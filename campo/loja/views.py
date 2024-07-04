from django.shortcuts import render

# Create your views here.

def pesquisar(request):
    return render(request, 'template/pesquisar.html')

def cadastrar(request):
    return render(request, 'template/cadastrar.html')

def deletar(request):
    return render(request, 'template/deletar.html')