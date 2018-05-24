
from django.urls import path

from .views import listar_produtos
from .views import novo_produto
from .views import produtos_update
from .views import produtos_delete

from .views import listar_fornecedores
from .views import novo_fornecedor
from .views import fornecedor_update
from .views import fornecedor_delete


urlpatterns = [	
    path('lista/produto', listar_produtos, name="listar_produtos"),
    path('novo/produto', novo_produto, name="novo_produto"),
    path('update/produto/<int:id>', produtos_update, name="produtos_update"),
    path('delete/produto/<int:id>', produtos_delete, name="produtos_delete"),

    path('lista/fornecedor', listar_fornecedores, name="listar_fornecedores"),
    path('novo/fornecedor', novo_fornecedor, name="novo_fornecedor"),
    path('update/fornecedor/<int:id>', fornecedor_update, name="fornecedor_update"),
    path('delete/fornecedor/<int:id>', fornecedor_delete, name="fornecedor_delete"),
]
