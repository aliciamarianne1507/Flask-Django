from django.contrib import admin
from django.urls import path, include #importar o arquivo de urls da aplicação 

urlpatterns = [
    path('',include('app.urls')), #rota raiz
    path('crud/',include('app.urls')), #rota primaria crud
    path('admin/', admin.site.urls), #rota administrativa 
]
