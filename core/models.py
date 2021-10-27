
from django.db import models


class Clientes(models.Model):


    ESTADO_CHOICES = (
        ('PE', 'Pernambuco'),
        ('SP', 'São Paulo'),
        ('AL', 'Alagoas'),
        ('RJ', 'Rio de Janeiro'),
    )

    nome = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    localidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Compras(models.Model):
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')
    data_compra = models.DateField()

    def __str__(self):
        return self.data_compra

    class Meta:
        managed = False
        db_table = 'compras'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class Fabricantes(models.Model):
    fabricante = models.CharField(max_length=45)

    def __str__(self):
        return self.fabricante

    class Meta:
        managed = False
        db_table = 'fabricantes'
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'


class Medicos(models.Model):
    nome = models.CharField(max_length=45)
    crm = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'medicos'
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class Produtos(models.Model):
    produto = models.CharField(max_length=45)
    designacao = models.CharField(max_length=45)
    composicao = models.CharField(max_length=45)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2)
    id_tipo_produto = models.ForeignKey('TiposProdutos', models.DO_NOTHING, db_column='id_tipo_produto')
    id_fabricante = models.ForeignKey(Fabricantes, models.DO_NOTHING, db_column='id_fabricante')

    def __str__(self):
        return self.produto

    class Meta:
        managed = False
        db_table = 'produtos'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class ProdutosCompra(models.Model):
    id_compra = models.ForeignKey(Compras, models.DO_NOTHING, db_column='id_compra')
    id_produto = models.ForeignKey(Produtos, models.DO_NOTHING, db_column='id_produto')
    quantidade = models.IntegerField()

    def __str__(self):
        return self.id_compra

    class Meta:
        managed = False
        db_table = 'produtos_compra'
        verbose_name = 'Produto_Compra'
        verbose_name_plural = 'Produtos_Compras'


class ReceitasMedicas(models.Model):
    id_produto_compra = models.ForeignKey(ProdutosCompra, models.DO_NOTHING, db_column='id_produto_compra')
    id_medico = models.ForeignKey(Medicos, models.DO_NOTHING, db_column='id_medico')
    receita = models.CharField(max_length=45)

    def __str__(self):
        return self.receita

    class Meta:
        managed = False
        db_table = 'receitas_medicas'
        verbose_name = 'receita médica'
        verbose_name_plural = 'receitas médicas'


class TiposProdutos(models.Model):
    tipo = models.CharField(max_length=45)

    def __str__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = 'tipos_produtos'
        verbose_name = 'Tipo Produto'
        verbose_name_plural = 'Tipos Produtos'
