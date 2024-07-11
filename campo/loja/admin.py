from django.contrib import admin
from .models import Produto, Fornecedor
# Register your models here.

class Produtoadm(admin.ModelAdmin):
    list_display=("id", "name", "preco")

admin.site.register(Produto, Produtoadm)
admin.site.register(Fornecedor)