from django.db import models

# Create your models here.

class Produto(models.Model):
    name = models.CharField(max_length=150)
    preco = models.IntegerField()

    def __str__(self):
        return self.name
    
class Fornecedor(models.Model):
    name = models.CharField(max_length=150)
    endereco = models.CharField(max_length=60)

    def __str__(self):
        return self.name