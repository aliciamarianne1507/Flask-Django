from django.urls import path
from .views import *


#Rotas secundárias 


urlpatterns = [
    path('',listagem),
    path('listagem/',listagem),
    path('/selecao/<int:id>/',selecao),
    path('consulta/',consulta),
    path('ordenacao/<str:campo>/',ordenacao),
    path('insercao/',insercao),
    path('salvar_insercao/',salvar_insercao),
    path('edicao/<int:id>/',edicao),
    path('salvar_edicao/',salvar_edicao),
    path('delete/<int:id>/',delete),
    path('salvar_delete/', salvar_delete),
    path('graficos/',graficos),

]