import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Set random seeds for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

def load_signal_data(data_dir, file_list, max_length=200):
    """Load and normalize signal data"""
    signals = []
    
    for filename in file_list:
        filepath = os.path.join(data_dir, filename)
        # Read the signal data
        data = pd.read_csv(filepath, header=None, names=['x', 'y', 'z'])
        signal = data[['x', 'y', 'z']].values.astype(np.float32)
        
        # Normalize signal length
        if len(signal) > max_length:
            signal = signal[:max_length]
        elif len(signal) < max_length:
            # Pad with zeros
            padding = np.zeros((max_length - len(signal), 3), dtype=np.float32)
            signal = np.vstack([signal, padding])
        
        signals.append(signal)
    
    return np.array(signals)

def load_data(data_dir):
    """Load training and test data"""
    # Load training data
    train_df = pd.read_csv(os.path.join(data_dir, 'train.txt'))
    train_files = train_df['filename'].tolist()
    train_labels = train_df['label'].tolist()
    
    # Load test data
    test_df = pd.read_csv(os.path.join(data_dir, 'test.txt'))
    test_files = test_df['filename'].tolist()
    
    return train_files, train_labels, test_files

def create_model(input_shape, num_classes, dropout_rate=0.3):
    """Create feed-forward neural network model"""
    model = keras.Sequential([
        # Flatten the input
        layers.Flatten(input_shape=input_shape),
        
        # First hidden layer
        layers.Dense(256, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(dropout_rate),
        
        # Second hidden layer
        layers.Dense(128, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(dropout_rate),
        
        # Output layer
        layers.Dense(num_classes, activation='softmax')
    ])
    
    return model

def train_model(model, X_train, y_train, X_val, y_val, num_epochs=100, batch_size=32):
    """Train the neural network"""
    # Compile model
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Learning rate scheduler
    lr_scheduler = keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        patience=5,
        factor=0.5,
        min_lr=1e-7
    )
    
    # Early stopping
    early_stopping = keras.callbacks.EarlyStopping(
        monitor='val_accuracy',
        patience=15,
        restore_best_weights=True
    )
    
    # Model checkpoint
    checkpoint = keras.callbacks.ModelCheckpoint(
        'best_model_tensorflow.h5',
        monitor='val_accuracy',
        save_best_only=True,
        mode='max'
    )
    
    # Train the model
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=num_epochs,
        batch_size=batch_size,
        callbacks=[lr_scheduler, early_stopping, checkpoint],
        verbose=1
    )
    
    return history

def predict_test(model, X_test):
    """Make predictions on test data"""
    predictions = model.predict(X_test)
    predicted_labels = np.argmax(predictions, axis=1)
    return predicted_labels

def main():
    # Configuration
    data_dir = 'data'
    max_length = 200  # Normalize all signals to this length
    batch_size = 32
    num_epochs = 100
    
    print("Using TensorFlow version:", tf.__version__)
    
    # Check if GPU is available
    if tf.config.list_physical_devices('GPU'):
        print("GPU available - using GPU acceleration")
    else:
        print("Using CPU")
    
    # Load data
    print("Loading data...")
    train_files, train_labels, test_files = load_data(data_dir)
    
    # Load and preprocess training signals
    print("Loading training signals...")
    X_train_full = load_signal_data(data_dir, train_files, max_length)
    y_train_full = np.array(train_labels)
    
    # Split training data into train and validation
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_full, y_train_full, 
        test_size=0.2, 
        random_state=42, 
        stratify=y_train_full
    )
    
    # Load test signals
    print("Loading test signals...")
    X_test = load_signal_data(data_dir, test_files, max_length)
    
    print(f"Training data shape: {X_train.shape}")
    print(f"Validation data shape: {X_val.shape}")
    print(f"Test data shape: {X_test.shape}")
    
    # Create model
    input_shape = (max_length, 3)  # 200 samples, 3 axes
    num_classes = 4  # Labels 0, 1, 2, 3
    model = create_model(input_shape, num_classes)
    
    # Display model summary
    print("\nModel Architecture:")
    model.summary()
    
    print(f"\nModel parameters: {model.count_params():,}")
    
    # Train model
    print("\nTraining model...")
    history = train_model(model, X_train, y_train, X_val, y_val, num_epochs, batch_size)
    
    # Load best model
    model.load_weights('best_model_tensorflow.h5')
    
    # Evaluate on validation set
    val_loss, val_accuracy = model.evaluate(X_val, y_val, verbose=0)
    print(f"\nBest validation accuracy: {val_accuracy*100:.2f}%")
    
    # Make predictions on test set
    print("Making predictions on test set...")
    test_predictions = predict_test(model, X_test)
    
    # Save predictions
    results_df = pd.DataFrame({
        'filename': test_files,
        'predicted_label': test_predictions
    })
    
    results_df.to_csv('predictions_tensorflow.txt', index=False, header=False)
    print("Predictions saved to predictions_tensorflow.txt")
    
    # Final evaluation
    print(f"\nFinal validation accuracy: {val_accuracy*100:.2f}%")
    
    if val_accuracy >= 0.85:
        print("🎉 Excellent! Accuracy >= 85% - You get 2 points!")
    elif val_accuracy >= 0.80:
        print("👍 Good! Accuracy >= 80% - You get 1 point!")
    else:
        print("⚠️  Accuracy < 80% - Need to improve the model")
    
    # Plot training history
    try:
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(12, 4))
        
        plt.subplot(1, 2, 1)
        plt.plot(history.history['accuracy'], label='Training Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        
        plt.subplot(1, 2, 2)
        plt.plot(history.history['loss'], label='Training Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title('Model Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        
        plt.tight_layout()
        plt.savefig('training_history.png', dpi=300, bbox_inches='tight')
        print("Training history plot saved as training_history.png")
        
    except ImportError:
        print("Matplotlib not available - skipping plot generation")

if __name__ == "__main__":
    main() 