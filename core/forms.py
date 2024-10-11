from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'Digite o nome do cliente'
        })
        self.fields['cpf'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': '999.999.999-99'
        })
        self.fields['telefone_celular'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': '(99) 99999-9999'
        })
        self.fields['data_nascimento'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'DD/MM/AAAA'
        })
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full'
            })

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'Digite o nome do funcionário'
        })
        self.fields['cpf'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': '999.999.999-99'
        })
        self.fields['telefone_celular'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': '(99) 99999-9999'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'email@exemplo.com'
        })
        self.fields['data_nascimento'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'DD/MM/AAAA'
        })
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full'
            })

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'Digite o nome do produto'
        })
        self.fields['valor_venda'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': '0.00'
        })
        self.fields['quantidade_estoque'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'Digite a quantidade'
        })
        self.fields['marca'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full'
        })
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full'
            })

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'Digite o nome do fornecedor'
        })
        self.fields['cnpj'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': '99.999.999/9999-99'
        })
        self.fields['telefone_celular'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': '(99) 99999-9999'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'email@exemplo.com'
        })
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full'
            })

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({
            'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full',
            'placeholder': 'Digite o nome da marca'
        })