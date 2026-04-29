import numpy as np

def transformar(df):
    # eliminar columna objetivo si existe
    if 'Rendimiento_General' in df.columns:
        df = df.drop(columns=['Rendimiento_General'])

    return np.array(df, dtype=float)