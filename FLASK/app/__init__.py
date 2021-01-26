#construtor da aplicação

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy #Conexação do Flask com o banco de dados
from flask_script import Manager #Gerencia as execuções do projeto
from flask_migrate import Migrate, MigrateCommand #Migração de dados 


app = Flask (__name__)
app.config.from_object('config') #busca o arquivo de configuração 

db = SQLAlchemy(app) #comunicação do Flask com o BD

migrate = Migrate(app,db) #Efetivar a migração do codigo python com o banco de dados 

manager = Manager(app)
manager.add_command('db',MigrateCommand)

from app.controlers import default
