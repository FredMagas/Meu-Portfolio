from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    media = models.CharField(max_length=100)
    mensagem = models.TextField(350)