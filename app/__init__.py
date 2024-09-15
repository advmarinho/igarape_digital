import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Inicializar o objeto db fora da função para evitar importação circular
db = SQLAlchemy()

def create_app():
    # Define o caminho para a pasta templates corretamente
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    CORS(app)

    # Configuração da conexão com o banco de dados MariaDB na AWS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://andersons:rootroot2@gerenciamentolivros.cxboev8t3ieu.us-east-1.rds.amazonaws.com:3306/gerenciamento_livros'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar o db com o aplicativo
    db.init_app(app)

    # Importar e registrar as rotas
    with app.app_context():
        from .routes import register_routes  # Use a notação de ponto para importar as rotas
        register_routes(app)
        db.create_all()  # Criar as tabelas se ainda não existirem

    return app
