from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField()
    empresa = models.CharField(max_length=40)
    telefone = models.CharField(max_length=20)
    media = models.CharField(max_length=100)
    mensagem = models.TextField(350)

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    technologies = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.title
