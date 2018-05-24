from django.contrib import admin
from .models import Produtos, Fornecedor

#ADICIONANDO COISAS NO ADMIN
admin.site.register(Produtos)
admin.site.register(Fornecedor)

# Register your models here.
