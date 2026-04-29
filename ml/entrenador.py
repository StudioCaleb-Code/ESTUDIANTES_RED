import pandas as pd
import numpy as np
import tensorflow as tf
from keras import layers
from sklearn.preprocessing import StandardScaler
import joblib
import os

def entrenar_neuronal_red():
    # 1. Verificar si existe la carpeta
    if not os.path.exists('models'):
        os.makedirs('models')

    # 2. Cargar los datos
    print("Cargando datos...")
    df = pd.read_csv('data/dataset_ml.csv')
    
    # 3. Separar X (datos) e y (Rendimiento_General: 0, 1, 2)
    X = df.drop('Rendimiento_General', axis=1)
    y = df['Rendimiento_General']
    
    # 4. Escalar los datos (La red neuronal trabaja mejor con datos normalizados)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 5. Definir la Arquitectura de la Red
    # Usamos 3 capas: Entrada, Oculta y Salida
    model = tf.keras.Sequential([
        layers.Input(shape=(X.shape[1],)), # Entrada con 20 neuronas (una por columna)
        layers.Dense(32, activation='relu'), # Capa oculta con 32 neuronas
        layers.Dense(16, activation='relu'), # Capa oculta con 16 neuronas
        layers.Dense(3, activation='softmax') # Salida: 3 neuronas (Bajo, Medio, Alto)
    ])
    
    # 6. Compilar el modelo
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 7. Entrenar la red
    print("Iniciando entrenamiento (Aprendizaje Supervisado)...")
    # Hacemos 150 vueltas (epochs) para que aprenda bien los patrones
    model.fit(X_scaled, y, epochs=150, verbose=1)
    
    # 8. Guardar la inteligencia (modelo) y el escalador
    model.save('models/red_estudiantes.h5')
    joblib.dump(scaler, 'models/escalador.pkl')
    
    print("\n--- ¡ENTRENAMIENTO COMPLETADO! ---")
    print("Modelo guardado en: models/red_estudiantes.h5")

if __name__ == "__main__":
    entrenar_neuronal_red()