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
