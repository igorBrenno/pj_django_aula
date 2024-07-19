from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
# Create your views here.

def pesquisar(request):
    if (request.method == "POST"):
        pesquisa = request.POST.get("pesquisa")
        print(pesquisa)
        resp = Produto.objects.filter(name__contains=pesquisa)
        return render(request, "loja/pesquisar.html", {'resultado':resp})

    resp = Produto.objects.all()
    # return HttpResponse(resp)
    return render(request, "loja/pesquisar.html", {'resultado':resp})

def cadastrar(request):
    
    return render(request, 'loja/cadastrar.html', {})

def deletar(request):
    return render(request, 'template/deletar.html')