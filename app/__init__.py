from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config  # configuración desde config.py

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints (rutas organizadas por módulo)
    from app.routes.auth_routes import auth_bp
    from app.routes.invoice_routes import invoice_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(invoice_bp, url_prefix="/invoices")

    return app
