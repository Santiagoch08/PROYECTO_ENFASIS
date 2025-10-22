from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL

mysql = MySQL()  # Instancia global

def create_app():
    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'CODESA'

    CORS(app, resources={r"/*": {"origins": "*"}})

    mysql.init_app(app)  # Inicializar extensión aquí

    # Importar blueprint *ya definido* con todas sus rutas
    from app.routes.index import main
    app.register_blueprint(main)
    from app.routes.enfasis import emphasis
    app.register_blueprint(emphasis)
    return app
