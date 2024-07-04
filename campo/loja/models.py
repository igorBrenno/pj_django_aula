from django.db import models

# Create your models here.

class Produto(models.Model):
    name = models.CharField(max_length=150)
    preço = models.IntegerField()

    
