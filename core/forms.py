from django import forms
from .models import Cliente, Funcionario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border border-zinc-700 bg-zinc-800 text-white gap-2 p-4 rounded focus:outline-none focus:border-blue-600 w-full'
            })

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border border-zinc-700 bg-zinc-800 text-white p-4 rounded focus:outline-none focus:border-blue-600 w-full'
            })
