from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
# Create your views here.

def pesquisar(request):

    resp = Produto.objects.filter(name="Empada")
    return HttpResponse(resp)

def cadastrar(request):
    return render(request, 'template/cadastrar.html')

def deletar(request):
    return render(request, 'template/deletar.html')