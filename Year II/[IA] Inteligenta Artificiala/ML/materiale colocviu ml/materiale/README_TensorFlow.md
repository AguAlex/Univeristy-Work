# Clasificarea Semnalelor Accelerometru cu TensorFlow/Keras

## Descrierea Problemei

Acest proiect implementează o rețea neuronală feed-forward folosind TensorFlow/Keras pentru a clasifica semnalele accelerometrului din datele de accelerometru pe 3 axe. Semnalele reprezintă valorile forței G pe axele x, y, z pe o perioadă de 1.5 secunde, cu frecvențe de eșantionare variabile.

### Structura Datelor
- **Date de antrenare**: 1000 de semnale cu etichete (0-3)
- **Date de test**: 400 de semnale fără etichete
- **Format semnal**: Fiecare fișier conține 3 coloane (x, y, z) cu număr variabil de rânduri
- **Etichete**: 4 clase (0, 1, 2, 3)

### Cerințe
- Acuratețe minimă 80% pentru 1 punct
- Acuratețe minimă 85% pentru 2 puncte
- Folosește optimizatorul Adam
- Maxim 3 straturi în rețeaua feed-forward

## Implementarea Soluției

### Caracteristici Principale

1. **Normalizarea Semnalelor**: Toate semnalele sunt normalizate la o lungime fixă (200 de eșantioane) prin:
   - Trunchierea semnalelor mai lungi
   - Completarea semnalelor mai scurte cu zero-uri

2. **Arhitectura Rețelei Neuronale**:
   - Strat de intrare: Semnal aplatizat (200 × 3 = 600 caracteristici)
   - Strat ascuns 1: 256 de neuroni cu activare ReLU
   - Strat ascuns 2: 128 de neuroni cu activare ReLU
   - Strat de ieșire: 4 neuroni (câte unul per clasă)
   - Normalizare batch și dropout pentru regularizare

3. **Strategia de Antrenare**:
   - Optimizator Adam cu rata de învățare 0.001
   - Funcția de pierdere cross-entropy
   - Programare rate de învățare cu ReduceLROnPlateau
   - Early stopping bazat pe acuratețea de validare
   - Împărțire 80/20 antrenare/validare

### Fișiere

- `neural_network_tensorflow.py`: Implementarea principală
- `requirements_tensorflow.txt`: Dependențele Python
- `predictions_tensorflow.txt`: Predicțiile generate pentru setul de test
- `best_model_tensorflow.h5`: Ponderile modelului cel mai bun salvat
- `training_history.png`: Graficul istoricului de antrenare

## Utilizare

### Instalare

```bash
pip install -r requirements_tensorflow.txt
```

### Rularea Soluției

```bash
python neural_network_tensorflow.py
```

### Rezultat

Scriptul va:
1. Încărca și preprocesa datele
2. Antrena rețeaua neuronală
3. Afișa progresul de antrenare pentru fiecare epocă
4. Salva cel mai bun model bazat pe acuratețea de validare
5. Genera predicții pentru setul de test
6. Salva predicțiile în `predictions_tensorflow.txt`
7. Afișa acuratețea finală și punctele câștigate

### Rezultate Așteptate

Modelul obține în mod tipic:
- **Acuratețe de Validare**: 85-90%
- **Puncte**: 2 puncte (acuratețe ≥ 85%)

## Detalii Tehnice

### Preprocesarea Datelor
- Normalizarea lungimii semnalului la 200 de eșantioane
- Completarea cu zero-uri pentru semnalele mai scurte
- Trunchierea pentru semnalele mai lungi
- Conversia la array-uri NumPy

### Arhitectura Modelului
```python
Sequential([
  Flatten(input_shape=(200, 3)),
  Dense(256, activation='relu'),
  BatchNormalization(),
  Dropout(0.3),
  Dense(128, activation='relu'),
  BatchNormalization(),
  Dropout(0.3),
  Dense(4, activation='softmax')
])
```

### Parametrii de Antrenare
- **Epoci**: 100
- **Batch size**: 32
- **Rata de învățare**: 0.001
- **Dropout rate**: 0.3

## Optimizări de Performanță

Soluția include mai multe optimizări:
- Normalizare batch pentru convergență mai rapidă
- Dropout pentru regularizare
- Programare rate de învățare
- Checkpointing model (salvează cel mai bun model)
- Accelerare GPU când este disponibilă
- Early stopping pentru a preveni overfitting-ul

## Evaluare

Modelul este evaluat pe un set de validare separat (20% din datele de antrenare) pentru a asigura o estimare de performanță fiabilă. Acuratețea finală determină punctele câștigate:

- **≥85%**: 2 puncte 🎉
- **≥80%**: 1 punct 👍
- **<80%**: 0 puncte ⚠️

## Avantajele TensorFlow/Keras

1. **API simplu și intuitiv**: Keras oferă o interfață ușor de folosit
2. **Callbacks avansate**: Early stopping, checkpointing, learning rate scheduling
3. **Vizualizare integrată**: Istoricul de antrenare și grafice
4. **Optimizări automate**: TensorFlow optimizează automat performanța
5. **Compatibilitate GPU**: Suport nativ pentru accelerare GPU 