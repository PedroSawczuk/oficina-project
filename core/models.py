import uuid
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.utils import timezone


class Cliente(models.Model):
    SEX_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=9, choices=SEX_CHOICES)
    cpf = models.CharField(max_length=14, unique=True, validators=[
        RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message='CPF deve estar no formato 999.999.999-99')
    ])
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9, validators=[
        RegexValidator(regex=r'^\d{5}-\d{3}$', message='CEP deve estar no formato 99999-999')
    ])
    criado = models.DateTimeField(auto_now_add=True)
    telefone_celular = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\(\d{2}\)\d{5}-\d{4}$', message='Telefone celular deve estar no formato (99)99999-9999')
    ])
    telefone_fixo = models.CharField(max_length=14, validators=[
        RegexValidator(regex=r'^\(\d{2}\)\d{4}-\d{4}$', message='Telefone fixo deve estar no formato (99)9999-9999')
    ], blank=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, validators=[
        RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', message='CNPJ deve estar no formato 99.999.999/9999-99')
    ])
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9, validators=[
        RegexValidator(regex=r'^\d{5}-\d{3}$', message='CEP deve estar no formato 99999-999')
    ])
    criado = models.DateTimeField(auto_now_add=True)
    telefone_celular = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\(\d{2}\)\d{5}-\d{4}$', message='Telefone celular deve estar no formato (99)99999-9999')
    ])
    telefone_fixo = models.CharField(max_length=14, validators=[
        RegexValidator(regex=r'^\(\d{2}\)\d{4}-\d{4}$', message='Telefone fixo deve estar no formato (99)9999-9999')
    ], blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantidade_estoque = models.PositiveIntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    SEX_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=9, choices=SEX_CHOICES)
    cpf = models.CharField(max_length=14, unique=True, validators=[
        RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message='CPF deve estar no formato 999.999.999-99')
    ])
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9, validators=[
        RegexValidator(regex=r'^\d{5}-\d{3}$', message='CEP deve estar no formato 99999-999')
    ])
    criado = models.DateTimeField(auto_now_add=True)
    telefone_celular = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\(\d{2}\)\d{5}-\d{4}$', message='Telefone celular deve estar no formato (99)99999-9999')
    ])
    telefone_fixo = models.CharField(max_length=14, validators=[
        RegexValidator(regex=r'^\(\d{2}\)\d{4}-\d{4}$', message='Telefone fixo deve estar no formato (99)9999-9999')
    ], blank=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cargo = models.ForeignKey('Cargo', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Escolaridade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class OrdemServico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tecnico = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao_problema = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ordem {self.id} - {self.cliente.nome}"


class ItemOrdemServico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total_item = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Reduzir a quantidade do produto no estoque ao salvar o item da ordem de serviço
        if self.pk is None:
            self.produto.quantidade_estoque -= self.quantidade
            self.produto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto.nome} - Quantidade: {self.quantidade}"


class ContaReceber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Conta a Receber - OS: {self.ordem_servico.id} - Valor: {self.valor}"


class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True, validators=[
        RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', message='CNPJ deve estar no formato 99.999.999/9999-99')
    ])
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9, validators=[
        RegexValidator(regex=r'^\d{5}-\d{3}$', message='CEP deve estar no formato 99999-999')
    ])
    criado = models.DateTimeField(auto_now_add=True)
    telefone_celular = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\(\d{2}\)\d{5}-\d{4}$', message='Telefone celular deve estar no formato (99)99999-9999')
    ])
    telefone_fixo = models.CharField(max_length=14, validators=[
        RegexValidator(regex=r'^\(\d{2}\)\d{4}-\d{4}$', message='Telefone fixo deve estar no formato (99)9999-9999')
    ], blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
