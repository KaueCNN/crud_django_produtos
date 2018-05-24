from django.forms import ModelForm
from .models import Produtos
from .models import Fornecedor



class ProdutosForm(ModelForm):
	class Meta:
		model = Produtos
		fields = ['fornecedor','nome_produto','desc_produto', 'tipo', 'valor']


class FornecedorForm(ModelForm):
	class Meta:
		model = Fornecedor
		fields = ['empresa','nome_prop','telefone', 'email', 'tipo_fornecedor']





			