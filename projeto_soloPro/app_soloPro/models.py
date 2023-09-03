from django.db import models


class Pessoa(models.Model):

    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)
    endereco = models.CharField(max_length=100)
    


    def __str__(self):
        return self.nome 


class Candidato(models.Model):

    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    proficao = models.CharField(max_length=200)
    contato = models.CharField(max_length=200)
    


    def __str__(self):
        return self.nome 


class Vaga(models.Model):

    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    atuacao = models.CharField(max_length=200)
    contato = models.CharField(max_length=200)
    


    def __str__(self):
        return self.nome 




