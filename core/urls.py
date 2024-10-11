from django.urls import *
from core.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="homePage"),

    path('clientes/', ClienteListView.as_view(), name='clienteList'), 
    path('clientes/novo/', ClienteCreateView.as_view(), name='clienteCreate'), 
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='clienteUpdate'),
    path('clientes/excluir/<int:pk>/', ClienteDeleteView.as_view(), name='clienteDelete'),

    path('funcionarios/', FuncionarioListView.as_view(), name='funcionarioList'),
    path('funcionarios/novo/', FuncionarioCreateView.as_view(), name='funcionarioCreate'),
    path('funcionarios/editar/<int:pk>/', FuncionarioUpdateView.as_view(), name='funcionarioUpdate'),
    path('funcionarios/excluir/<int:pk>/', FuncionarioDeleteView.as_view(), name='funcionarioDelete'),

    path('produtos/', ProdutoListView.as_view(), name='produtoList'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produtoCreate'),
    path('produtos/editar/<int:pk>/', ProdutoUpdateView.as_view(), name='produtoUpdate'),
    path('produtos/excluir/<int:pk>/', ProdutoDeleteView.as_view(), name='produtoDelete'),

    path('fornecedores/', FornecedorListView.as_view(), name='fornecedorList'),
    path('fornecedores/novo/', FornecedorCreateView.as_view(), name='fornecedorCreate'),
    path('fornecedores/editar/<int:pk>/', FornecedorUpdateView.as_view(), name='fornecedorUpdate'),
    path('fornecedores/excluir/<int:pk>/', FornecedorDeleteView.as_view(), name='fornecedorDelete'),

    path('marcas/', MarcaListView.as_view(), name='marcaList'),
    path('marcas/novo/', MarcaCreateView.as_view(), name='marcaCreate'),
    path('marcas/editar/<int:pk>/', MarcaUpdateView.as_view(), name='marcaUpdate'),
    path('marcas/excluir/<int:pk>/', MarcaDeleteView.as_view(), name='marcaDelete'),

]
