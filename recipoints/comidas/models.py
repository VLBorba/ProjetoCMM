from django.db import models

class home(models.Model):
    nome = 'Recipoints'
    variaveis = models.URLField(max_length=200)

class bares(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True,default="Não Encontrado")
    bairro = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    horario = models.TimeField(null=False, blank=False)
    distancia = models.IntegerField(null=True)
    inaugurado = models.DateField(null=True)

class comidas(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True,default="Não Encontrado")
    bairro = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    horario = models.TimeField(null=False, blank=False)
    distancia = models.IntegerField(null=True)
    inaugurado = models.DateField(null=True)

class cinemas(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True,default="Não Encontrado")
    bairro = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    horario = models.TimeField(null=False, blank=False)
    distancia = models.IntegerField(null=True)
    site = models.URLField(max_length=200)

class lazer(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True,default="Não Encontrado")
    bairro = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    horario = models.TimeField(null=False, blank=False)
    distancia = models.IntegerField(null=True)
    site = models.URLField(max_length=200)

class praias(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True,default="Não Encontrado")
    bairro = models.CharField(max_length=20, null=False, blank=False)
    referencial = models.CharField(max_length=50, null=False, blank=False)
    distancia = models.IntegerField(null=True)

class turismo(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True,default="Não Encontrado")
    bairro = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    horario = models.TimeField(null=False, blank=False)
    distancia = models.IntegerField(null=True)
    site = models.URLField(max_length=200) 