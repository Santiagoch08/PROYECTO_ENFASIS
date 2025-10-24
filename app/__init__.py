import pymysql
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecretkey"  # ⚠️ cámbiala por una segura

    # Configuración de conexión a MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/CODESA'
    app.config['SQLALCHEMY_TRACKfrom app import db_MODIFICATIONS'] = False

    # Inicializar la base de datos con la app
    db.init_app(app)

    # Permitir CORS
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Registrar blueprints
    from app.routes.enfasis import emphasis
    from app.routes.rol import rol_bp
    from app.routes.index import main

    app.register_blueprint(emphasis)
    app.register_blueprint(rol_bp)
    app.register_blueprint(main)

    # Crear tablas si no existen
    with app.app_context():
        db.create_all()

    return app
