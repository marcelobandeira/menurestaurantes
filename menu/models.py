# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dono(models.Model):
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	senha = models.CharField(max_length=256)
	telefone = models.CharField(max_length=12)

class Restaurante(models.Model):
	nome = models.CharField(max_length=100)
	endereco = models.CharField(max_length=300)
	telefone = models.CharField(max_length=12)
	foto = models.CharField(max_length=100)
	dono = models.ForeignKey(Dono, on_delete=models.CASCADE, related_name = 'restaurantes')

class Categoria(models.Model):
	nome = models.CharField(max_length=100)
	restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='categorias')

class Opcao(models.Model):
	nome = models.CharField(max_length=100)
	preco = models.DecimalField(max_digits=6, decimal_places=2)
	likes = models.IntegerField()
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='opcoes')

class Foto(models.Model):
	path = models.CharField(max_length=100)
	opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE, related_name='fotos')

class Cliente(models.Model):
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	senha = models.CharField(max_length=256)
	foto = models.CharField(max_length=100)
	facebook = models.CharField(max_length=100)
	favoritos = models.ManyToManyField(Opcao, related_name='fav_by')
	avaliacoes = models.ManyToManyField(Opcao, through='Avaliacao')

class Avaliacao(models.Model):
	avaliacao = models.IntegerField()
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)

class Cobertura(models.Model):
	descricao = models.CharField(max_length=50)
	
	def __str__(self):
		return self.descricao

class Pizza(models.Model):
	nome = models.CharField(max_length=50)
	coberturas = models.ManyToManyField(Cobertura)
