from django.db import models


class Fornecedor(models.Model):
	id = models.AutoField(primary_key=True)
	empresa = models.CharField(max_length=40)
	nome_prop = models.CharField(max_length=50)
	telefone = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	tipo_fornecedor = models.CharField(max_length=50)

	def __str__(self):
		return self.empresa 	


class Produtos(models.Model):
	id = models.AutoField(primary_key=True)
	fornecedor = models.ManyToManyField(Fornecedor, blank=True)
	nome_produto = models.CharField(max_length=100)
	desc_produto = models.CharField(max_length=100)
	tipo = models.CharField(max_length=100)
	valor = models.DecimalField(max_digits=6, decimal_places=2)


	def __str__(self):
		return self.nome_produto








