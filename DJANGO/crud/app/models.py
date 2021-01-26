from django.db import models

class Pessoa (models.Model):
    # A coluna id é criada automaticamente pelo Django 
    nome = models.CharField(max_length=100)     #campo que armazena caracteres
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    salario = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome