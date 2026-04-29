import os
from flask import Flask

def create_app():
    # Configuramos las rutas para que encuentre los archivos en la raíz
    template_dir = os.path.abspath('templates')
    static_dir = os.path.abspath('static')
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app