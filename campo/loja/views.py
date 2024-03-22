from django.shortcuts import render

# Create your views here.

def pesquisar(request):
    return render(request, 'template_loja/loja.html')

def cadastrar(request):
    return render(request, 'template_loja/cadastrar.html', {})