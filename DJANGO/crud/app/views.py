#Codificação dos controladores

from django.shortcuts import render #renderizar os templates 
from .models import Pessoa
from django.views.decorators.csrf import csrf_protect  #validação dos tokens que serão enviados pelos métodos post dos formulários 


def listagem(request):
    pessoas = Pessoa.objects.all() 
    return render(request,'listagem.html', {'pessoas':pessoas})

def selecao(request,id=0):
    pessoa = Pessoa.objects.get(id=id) #Filtro
    return render(request,'listagem.html',{'pessoas':[pessoa]})


_campo = ''
def ordenacao(request,campo='id'):
    global _campo

    if campo == _campo:
        pessoas = Pessoa.objects.all().order_by(campo).reverse()
        _campo =''
    else:
        pessoas = Pessoa.objects.all().order_by(campo)
        _campo = campo
    return render(request,'listagem.html',{'pessoas': pessoas})


@csrf_protect #validar o token - funções que serão acionadas por métodos post
def consulta(request):
    consulta = request.POST.get('consulta')   #consultas completas ou parciais 
    campo= request.POST.get('campo') #vem de um select do html 

    if campo == 'nome':
        pessoas = Pessoa.objects.filter(nome__contains = consulta)
    elif campo == 'idade':
        pessoas = Pessoa.objects.filter(idade__contains = consulta)
    elif campo == 'sexo':
        pessoas = Pessoa.objects.filter(sexo__contains = consulta)
    elif campo == 'salario':
        if consulta.find(',')>0 or consulta.find('.')>0:    #verfica se a string recebida possui alguma precisão decimal
            consulta = float(consulta.replace(',','.'))
        pessoas = Pessoa.objects.filter(salario__contains = consulta)
    else:
        pessoas = Pessoa.objects.all()
    
    return render(request,'listagem.html',{'pessoas': pessoas})

def insercao(request):
    return render(request,'insercao.html')

@csrf_protect #validar o token - funções que serão acionadas por métodos post
def salvar_insercao(request):
    Nome = request.POST.get('nome')
    Idade = request.POST.get('idade')
    Sexo = request.POST.get('sexo')
    Salario = request.POST.get('salario')
    Salario = Salario.replace(',','.')

    objeto = Pessoa(nome= Nome,idade = Idade,sexo =Sexo, salario = Salario) #criação do objeto 

    objeto.save() #efetica a inserção e nao precisa do commit como precisa no flask
    pessoas = Pessoa.objects.all()
    return render(request,'listagem.html',{'pessoas': pessoas})
#edição de registros:


def edicao(request, id=0):
    pessoa = Pessoa.objects.get(id=id)
    return render(request,'edicao.html',{'pessoa' : pessoa})

@csrf_protect #validar o token - funções que serão acionadas por métodos post
def salvar_edicao(request):
    Id= request.POST.get('id')
    Nome = request.POST.get('nome')
    Idade = request.POST.get('idade')
    Sexo = request.POST.get('sexo')
    Salario = request.POST.get('salario')
    Salario = Salario.replace(',','.')

    Pessoa.objects.filter(id=Id).update(nome= Nome,idade = Idade,sexo =Sexo, salario = Salario)   #atualizar o registo

    pessoas = Pessoa.objects.all()
    return render(request,'listagem.html', {'pessoas': pessoas})

#rotas de delete


def delete(request,id=0):
    pessoa = Pessoa.objects.get(id=id)
    return render(request,'delete.html',{'pessoa' : pessoa})

@csrf_protect #validar o token - funções que serão acionadas por métodos post
def salvar_delete(request):
    Id= request.POST.get('id')

    Pessoa.objects.filter(id=Id).delete() #deleta o dado pelo id
    pessoas = Pessoa.objects.all()
    return render(request,'listagem.html', {'pessoas': pessoas})



#carregamento dos gráficos 

def graficos(request):
    pessoasM= Pessoa.objects.filter(sexo='M')
    pessoasF= Pessoa.objects.filter(sexo='F')
    pessoas = Pessoa.objects.all()

    salarioM = 0
    for m in pessoasM:
        salarioM += m.salario 
    if len(pessoasM) >0 :
        salarioM = salarioM/len(pessoasM) #média salarial 
    salarioF = 0
    for f in pessoasF:
        salarioF += f.salario 
    if len(pessoasF) >0 :
        salarioF = salarioF/len(pessoasF) #média salarial 


    idadeM = 0
    for m in pessoasM:
        idadeM += m.idade
    if len(pessoasM) >0 :
        idadeM = idadeM/len(pessoasM) #média salarial 
    idadeF = 0
    for f in pessoasF:
        idadeF += f.idade 
    if len(pessoasF) >0 :
        idadeF = idadeF/len(pessoasF) #média salarial 
    
    IDs=[]
    Idades =[]
    for p in pessoas:
        IDs.append(p.id)
        Idades.append(p.idade)
    
    return render(request,'graficos.html', {'salarioM' : salarioM, 'salarioF' : salarioF, 'idadeM' : idadeM, 'idadeF': idadeF,'IDs' : IDs, 'Idades': Idades})