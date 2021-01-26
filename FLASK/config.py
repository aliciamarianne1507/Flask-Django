#Configuração da aplicação 

import os.path

basedir = os.path.abspath(os.path.dirname(__file__)) #Pega o caminho da aplicação 

DEBUG = True 
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir,'banco.db') #Definição do diretório onde está o banco de dados
SQLALCHEMY_TRACK_MODIFICATIONS = True #modificações no banco 