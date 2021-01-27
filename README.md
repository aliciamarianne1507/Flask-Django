# 🚀 Desenvolvimento Web com Flask e Django 

Aplicações desenvolvidas durante o curso "Desenvolvimento Web com Flask e Django" disponível na Udemy Academy através o link: https://www.udemy.com/course/desenvolvimento-web-com-flask-e-django/

## Sobre o projeto

O projeto consiste na criação de uma pagina Web que permite a inserção de dados, a visualização desses dados inseridos, edição, exclusão e visão gráfica. 

<img align="center" src="https://github.com/aliciamarianne1507/backup/blob/main/55.PNG">

## Instalação dos pacotes 

Eu já possuia o [Python](https://www.python.org/downloads/)pip instalados na minha maquina, caso não tenha você deve instala-lo pois a lógicas e rotas serão criadas em python. 
O editor utilizado para a elaboração dos scripts foi o [VS Code](https://code.visualstudio.com/download)

### Flask


#### Instalação dos pacotes 

No termininal ou prompt de comando faça:

```
pip install Flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-script

```

#### Criação do Projeto 

Para o Flask, os pacotes foram estruturados utilizando a arquitetura MVC: 

- Models - Modelo de dados para conectar com o Banco de Dados 
- Views ou Templates - Visualização HTML 
- Controllers - Controle da Aplicação

##### Outros comandos importantes:

Execução do servidor:

```
python run.py runserver

```


### Django

#### Instalação do Django

No termininal ou prompt de comando faça:

```
pip install Django

```
#### Criação do Projeto 


No Django, ao utilizar o comando:

```
django-admin startproject nome_do_projeto

```
O próprio Django já cria toda a estrutura para o desenvolvimento do app. 

##### Outros comandos importantes:

Execução do servidor:

```
python manage.py runserver

```

Criação do aplicativo:

```
python manage.py startapp nome_do_app

```

Criação da classe de tabela:

```
python manage.py makemigrations

```

Criação das tabelas no banco:

```
python manage.py migrate

```

Criação do super usuário:

```
python manage.py createsuperuser

```











