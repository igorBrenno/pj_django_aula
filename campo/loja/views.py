from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pesquisar(request):
    return HttpResponse("Estou")

def cadastrar(request):
    return render(request, 'template/cadastrar.html')

def deletar(request):
    return render(request, 'template/deletar.html')