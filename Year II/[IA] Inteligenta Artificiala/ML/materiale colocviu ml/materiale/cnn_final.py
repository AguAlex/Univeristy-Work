import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping
import numpy as np

# Setam dimensiunea imaginilor si marimea batch-ului
dimensiune_imagine = (100, 100)
batch_size = 32

# Incarcam fisierele CSV pentru antrenare, validare si test
date_antrenare = pd.read_csv("../data/train.csv")
date_validare = pd.read_csv("../data/validation.csv")
date_test = pd.read_csv("../data/test.csv")

# Adaugam o coloana fictiva 'label' in setul de test (necesara pentru generator)
date_test['label'] = 0

# Completam calea catre fisierele imagine
date_antrenare["image_id"] = date_antrenare["image_id"].apply(lambda x: os.path.join("../data/train", f"{x}.png"))
date_validare["image_id"] = date_validare["image_id"].apply(lambda x: os.path.join("../data/validation", f"{x}.png"))
date_test["image_id"] = date_test["image_id"].apply(lambda x: os.path.join("../data/test", f"{x}.png"))

# Convertim etichetele in string (cerinta pentru class_mode="sparse")
date_antrenare['label'] = date_antrenare['label'].astype(str)
date_validare['label'] = date_validare['label'].astype(str)

# Generator de imagini cu augmentare pentru antrenare
generator_antrenare = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Generator simplu (doar scalare) pentru validare si test
generator_validare = ImageDataGenerator(rescale=1./255)
generator_test = ImageDataGenerator(rescale=1./255)

# Creem obiectele pentru incarcarea imaginilor
flux_antrenare = generator_antrenare.flow_from_dataframe(
    date_antrenare, x_col="image_id", y_col="label",
    target_size=dimensiune_imagine, batch_size=batch_size, class_mode="sparse")

flux_validare = generator_validare.flow_from_dataframe(
    date_validare, x_col="image_id", y_col="label",
    target_size=dimensiune_imagine, batch_size=batch_size, class_mode="sparse")

flux_test = generator_test.flow_from_dataframe(
    date_test, x_col="image_id", y_col="label",
    target_size=dimensiune_imagine, batch_size=batch_size, class_mode=None, shuffle=False)

# Definim arhitectura retelei neuronale convolutionale
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(*dimensiune_imagine, 3)),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(256, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),

    layers.Flatten(),
    layers.Dense(256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    layers.Dropout(0.5),
    layers.Dense(5, activation='softmax')
])

# Compilam modelul
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Callback-uri pentru ajustarea automata a ratei de invatare si early stopping
ajustare_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Antrenam modelul pe setul de date
history = model.fit(
    flux_antrenare,
    validation_data=flux_validare,
    epochs=30,
    callbacks=[early_stopping, ajustare_lr]
)

# Generam predictii pe setul de test
predictii_probabilitati = model.predict(flux_test)
etichete_pred = np.argmax(predictii_probabilitati, axis=1)

# Cream DataFrame-ul pentru predicții
rezultat = pd.DataFrame({
    "image_id": date_test["image_id"].apply(lambda x: os.path.splitext(os.path.basename(x))[0]),
    "label": etichete_pred
})

# Salvam predictiile intr-un fisier CSV
rezultat.to_csv("submission_cnn2.csv", index=False)
