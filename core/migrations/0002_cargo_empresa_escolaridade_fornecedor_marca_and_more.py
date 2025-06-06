# Generated by Django 5.1.2 on 2024-10-09 14:16

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(message='CNPJ deve estar no formato 99.999.999/9999-99', regex='^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$')])),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='CEP deve estar no formato 99999-999', regex='^\\d{5}-\\d{3}$')])),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('telefone_celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Telefone celular deve estar no formato (99)99999-9999', regex='^\\(\\d{2}\\)\\d{5}-\\d{4}$')])),
                ('telefone_fixo', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message='Telefone fixo deve estar no formato (99)9999-9999', regex='^\\(\\d{2}\\)\\d{4}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(message='CNPJ deve estar no formato 99.999.999/9999-99', regex='^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$')])),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='CEP deve estar no formato 99999-999', regex='^\\d{5}-\\d{3}$')])),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('telefone_celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Telefone celular deve estar no formato (99)99999-9999', regex='^\\(\\d{2}\\)\\d{5}-\\d{4}$')])),
                ('telefone_fixo', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message='Telefone fixo deve estar no formato (99)9999-9999', regex='^\\(\\d{2}\\)\\d{4}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='criadoEm',
            new_name='criado',
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='CEP deve estar no formato 99999-999', regex='^\\d{5}-\\d{3}$')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='CPF deve estar no formato 999.999.999-99', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone_celular',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Telefone celular deve estar no formato (99)99999-9999', regex='^\\(\\d{2}\\)\\d{5}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone_fixo',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message='Telefone fixo deve estar no formato (99)9999-9999', regex='^\\(\\d{2}\\)\\d{4}-\\d{4}$')]),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=9)),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='CPF deve estar no formato 999.999.999-99', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')])),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='CEP deve estar no formato 99999-999', regex='^\\d{5}-\\d{3}$')])),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('telefone_celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Telefone celular deve estar no formato (99)99999-9999', regex='^\\(\\d{2}\\)\\d{5}-\\d{4}$')])),
                ('telefone_fixo', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message='Telefone fixo deve estar no formato (99)9999-9999', regex='^\\(\\d{2}\\)\\d{4}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao_problema', models.TextField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='ContaReceber',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ordemservico')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('quantidade_estoque', models.PositiveIntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='core.marca')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrdemServico',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantidade', models.PositiveIntegerField()),
                ('valor_total_item', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.ordemservico')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto')),
            ],
        ),
    ]
