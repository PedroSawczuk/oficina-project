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

]
