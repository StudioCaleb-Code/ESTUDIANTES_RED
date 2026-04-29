from flask import Blueprint, render_template, request
import pandas as pd
from ml.modelo import predecir_estudiantes # Importamos tu lógica de IA

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/formulario')
def formulario():
    return render_template('formulario.html')

@main_bp.route('/procesar', methods=['POST'])
def procesar():
    if 'file' not in request.files:
        return "No hay archivo", 400
    
    file = request.files['file']
    df = pd.read_csv(file)
    
    # Aquí llamamos a la red neuronal
    resultados, resumen, recomendaciones = predecir_estudiantes(df)
    
    return render_template('resultado.html', 
                           resultados=resultados, 
                           resumen=resumen, 
                           recomendaciones=recomendaciones)