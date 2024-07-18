from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
# Create your views here.

def pesquisar(request):

    resp = Produto.objects.all()
    # return HttpResponse(resp)
    return render(request, "loja/pesquisar.html", {'resultado':resp})

def cadastrar(request):
    
    return render(request, 'loja/cadastrar.html', {})

def deletar(request):
    return render(request, 'template/deletar.html')