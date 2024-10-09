from django.contrib import admin
from .models import Cliente, Fornecedor, Marca, Produto, Funcionario, Cargo, OrdemServico, ItemOrdemServico, ContaReceber, Empresa

# Customizando a listagem dos Clientes
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone_celular', 'email', 'criado')  # Campos a serem exibidos na listagem
    search_fields = ('nome', 'cpf', 'email')  # Campos para busca
    list_filter = ('sexo', 'criado')  # Filtros na lateral
    ordering = ('-criado',)  # Ordenar por data de criação (mais recentes primeiro)
    date_hierarchy = 'criado'  # Adiciona um hierarquia de datas
    readonly_fields = ('criado',)  # Campos somente leitura no form
    fieldsets = (
        (None, {'fields': ('nome', 'sexo', 'cpf', 'data_nascimento')}),
        ('Endereço', {'fields': ('rua', 'bairro', 'numero', 'cep')}),
        ('Contato', {'fields': ('telefone_celular', 'telefone_fixo', 'email')}),
        ('Informações Adicionais', {'fields': ('criado',)}),
    )


# Customizando a listagem dos Fornecedores
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone_celular', 'email', 'criado')
    search_fields = ('nome', 'cnpj', 'email')
    list_filter = ('criado',)
    ordering = ('-criado',)
    readonly_fields = ('criado',)
    fieldsets = (
        (None, {'fields': ('nome', 'cnpj')}),
        ('Endereço', {'fields': ('rua', 'bairro', 'numero', 'cep')}),
        ('Contato', {'fields': ('telefone_celular', 'telefone_fixo', 'email')}),
        ('Informações Adicionais', {'fields': ('criado',)}),
    )


# Customizando Marcas
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)


# Customizando Produtos
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_venda', 'quantidade_estoque', 'marca')
    search_fields = ('nome', 'marca__nome')
    list_filter = ('marca',)
    ordering = ('nome',)
    actions = ['atualizar_estoque']

    # Ação personalizada para atualizar o estoque em massa
    def atualizar_estoque(self, request, queryset):
        for produto in queryset:
            produto.quantidade_estoque += 10  # Adiciona 10 itens ao estoque
            produto.save()
        self.message_user(request, "Estoque atualizado com sucesso!")
    atualizar_estoque.short_description = "Atualizar estoque (adicionar 10 unidades)"


# Customizando Funcionários
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cargo', 'telefone_celular', 'email', 'criado')
    search_fields = ('nome', 'cpf', 'email')
    list_filter = ('sexo', 'cargo', 'criado')
    ordering = ('-criado',)
    readonly_fields = ('criado',)
    fieldsets = (
        (None, {'fields': ('nome', 'sexo', 'cpf', 'data_nascimento', 'cargo')}),
        ('Endereço', {'fields': ('rua', 'bairro', 'numero', 'cep')}),
        ('Contato', {'fields': ('telefone_celular', 'telefone_fixo', 'email')}),
        ('Informações Adicionais', {'fields': ('criado',)}),
    )


# Customizando Cargos
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


# Customizando Ordens de Serviço
class ItemOrdemServicoInline(admin.TabularInline):
    model = ItemOrdemServico
    extra = 1  # Quantidade de itens extras ao criar
    fields = ('produto', 'quantidade', 'valor_total_item')


@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tecnico', 'cliente', 'data', 'valor_total')
    search_fields = ('tecnico__nome', 'cliente__nome')
    list_filter = ('data',)
    ordering = ('-data',)
    inlines = [ItemOrdemServicoInline]  # Itens da ordem de serviço inline
    readonly_fields = ('data', 'valor_total')
    fieldsets = (
        (None, {'fields': ('tecnico', 'cliente', 'descricao_problema')}),
        ('Detalhes', {'fields': ('data', 'valor_total')}),
    )


# Customizando Contas a Receber
@admin.register(ContaReceber)
class ContaReceberAdmin(admin.ModelAdmin):
    list_display = ('ordem_servico', 'valor')
    search_fields = ('ordem_servico__id',)
    ordering = ('-ordem_servico',)


# Customizando Empresa
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone_celular', 'email', 'criado')
    search_fields = ('nome', 'cnpj', 'email')
    list_filter = ('criado',)
    ordering = ('-criado',)
    readonly_fields = ('criado',)
    fieldsets = (
        (None, {'fields': ('nome', 'cnpj')}),
        ('Endereço', {'fields': ('rua', 'bairro', 'numero', 'cep')}),
        ('Contato', {'fields': ('telefone_celular', 'telefone_fixo', 'email')}),
        ('Informações Adicionais', {'fields': ('criado',)}),
    )
