from django.urls import *
from core.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="homePage"),

    path('clientes/novo/', ClienteCreateView.as_view(), name='clienteCreate'), 
    path('clientes/', ClienteListView.as_view(), name='clienteList'), 
    path('funcionarios/novo/', FuncionarioCreateView.as_view(), name='funcionarioCreate'), 
    path('funcionarios/', FuncionarioListView.as_view(), name='funcionarioList'), 

]
