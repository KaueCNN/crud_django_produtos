from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produtos
from .models import Fornecedor
from .forms import ProdutosForm
from .forms import FornecedorForm



######### FORNECEDOR #########


@login_required
def listar_fornecedores(request):
	fornecedores = Fornecedor.objects.all()
	return render(request, 'fornecedores.html', {'fornecedores': fornecedores})



@login_required
def novo_fornecedor(request):
	form = FornecedorForm(request.POST or None,request.FILES or None)

	if form.is_valid():
		form.save()
		return redirect('listar_fornecedores')

	return render(request, 'fornecedor_form.html', {'form': form})		

@login_required
def fornecedor_update(request, id):
	fornecedores = get_object_or_404(Fornecedor, pk=id)
	form = FornecedorForm(request.POST or None, request.FILES or None, instance=fornecedores)

	if form.is_valid():
		form.save()
		return redirect('listar_fornecedores')

	return render(request, 'fornecedor_form.html', {'form': form})	


@login_required
def fornecedor_delete(request, id):
	fornecedores = get_object_or_404(Fornecedor, pk=id)
	form = FornecedorForm(request.POST or None, request.FILES or None, instance=fornecedores)

	if request.method == 'POST':	
		fornecedores.delete()
		return redirect('listar_fornecedores')				

	return render(request, 'fornecedor_confirm_delete.html', {'fornecedores': fornecedores})


############ PRODUTOS ###############

@login_required
def listar_produtos(request):
	produtos =  Produtos.objects.all()
	return render(request, 'produtos.html', {'produtos': produtos})



@login_required
def novo_produto(request):
	form = ProdutosForm(request.POST or None,request.FILES or None)

	if form.is_valid():
		form.save()
		return redirect('listar_produtos')

	return render(request, 'produtos_form.html', {'form': form})



@login_required
def produtos_update(request, id):
	produtos = get_object_or_404(Produtos, pk=id)
	form = ProdutosForm(request.POST or None, request.FILES or None, instance=produtos)

	if form.is_valid():
		form.save()
		return redirect('listar_produtos')

	return render(request, 'produtos_form.html', {'form': form})



@login_required
def produtos_delete(request, id):
	produtos = get_object_or_404(Produtos, pk=id)
	form = ProdutosForm(request.POST or None, request.FILES or None, instance=produtos)

	if request.method == 'POST':	
		produtos.delete()
		return redirect('listar_produtos')				

	return render(request, 'produto_confirm_delete.html', {'produtos': produtos})

