from django.contrib import admin
from .models import Clientes, Fabricantes, Medicos, Produtos, ProdutosCompra, ReceitasMedicas, TiposProdutos


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'telefone', 'cep', 'cpf', 'localidade', 'estado', )


@admin.register(Fabricantes)
class FabricantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fabricante',)



@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)



@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'designacao', 'composicao', 'preco_venda', 'id_tipo_produto', 'id_fabricante', )



@admin.register(ProdutosCompra)
class ProdutosCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_compra', 'id_produto', 'quantidade', )


@admin.register(ReceitasMedicas)
class ReceitasMedicasCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_produto_compra', 'id_medico', 'receita', )



@admin.register(TiposProdutos)
class TiposProdutosCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo',)