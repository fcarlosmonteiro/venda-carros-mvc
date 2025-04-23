from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='views/templates')
    
    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carros.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
    
    # Inicialização das extensões
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registro das rotas
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Criação das tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    return app 