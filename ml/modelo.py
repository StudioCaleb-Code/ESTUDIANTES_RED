import pandas as pd
import numpy as np
import os
import tensorflow as tf
from keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Usamos el archivo .h5 que ya tienes en tu carpeta ml/
ruta_modelo = os.path.join(BASE_DIR, 'modelo_red.h5')

def predecir_estudiantes(df):
    try:
        # Cargar el modelo .h5 directamente
        if not os.path.exists(ruta_modelo):
            return [], {}, ["Error: No se encuentra modelo_red.h5 en ml/"]
            
        model = load_model(ruta_modelo)

        # Limpieza de datos
        # Quitamos la columna objetivo si existe y nos quedamos solo con números
        X_df = df.select_dtypes(include=[np.number]).drop(columns=['Rendimiento_General'], errors='ignore')
        
        # Convertir a array
        X = X_df.values.astype(np.float32)

        # Predicción masiva (más rápido que uno por uno en .h5)
        predicciones = model.predict(X)
        clases = np.argmax(predicciones, axis=1)

        # Mapeo
        mapping = {0: "Bajo", 1: "Medio", 2: "Alto"}
        resultados = [mapping.get(int(c), "Error") for c in clases]

        resumen = {
            "bajos": resultados.count("Bajo"),
            "medios": resultados.count("Medio"),
            "altos": resultados.count("Alto")
        }

        return resultados, resumen, ["Análisis exitoso con modelo Keras (.h5)"]

    except Exception as e:
        return [], {}, [f"Error en el modelo: {str(e)}"]