from django.shortcuts import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *

class HomePageView(TemplateView):
    template_name = 'homePage.html'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/clienteForm.html'
    success_url = reverse_lazy('clienteList') 

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/clienteList.html'
    context_object_name = 'clientes'

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/clienteForm.html'
    success_url = reverse_lazy('clienteList')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/clienteConfirmDelete.html'
    success_url = reverse_lazy('clienteList')

class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionarios/funcionarioForm.html'
    success_url = reverse_lazy('funcionarioList') 

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'funcionarios/funcionarioList.html'
    context_object_name = 'funcionarios'

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionarios/funcionarioForm.html'
    success_url = reverse_lazy('funcionarioList')

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'funcionarios/funcionarioConfirmDelete.html'
    success_url = reverse_lazy('funcionarioList')


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produtoForm.html'
    success_url = reverse_lazy('produtoList')

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produtoList.html'
    context_object_name = 'produtos'

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produtoForm.html'
    success_url = reverse_lazy('produtoList')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/produtoConfirmDelete.html'
    success_url = reverse_lazy('produtoList')

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedores/fornecedorForm.html'
    success_url = reverse_lazy('fornecedorList')

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'fornecedores/fornecedorList.html'
    context_object_name = 'fornecedores'

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedores/fornecedorForm.html'
    success_url = reverse_lazy('fornecedorList')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'fornecedores/fornecedorConfirmDelete.html'
    success_url = reverse_lazy('fornecedorList')

class MarcaListView(ListView):
    model = Marca
    template_name = 'marcas/marcaList.html'
    context_object_name = 'marcas'

class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marcas/marcaForm.html'
    success_url = reverse_lazy('marcaList')

class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marcas/marcaForm.html'
    success_url = reverse_lazy('marcaList')

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marcas/marcaConfirmDelete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('marcaList')
