# Generated by Django 3.2.8 on 2021-10-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=45)),
                ('telefone', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
                ('localidade', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_compra', models.DateField()),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'compras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fabricantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Fabricante',
                'verbose_name_plural': 'Fabricantes',
                'db_table': 'fabricantes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('crm', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
                'db_table': 'medicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=45)),
                ('designacao', models.CharField(max_length=45)),
                ('composicao', models.CharField(max_length=45)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'produtos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProdutosCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
            ],
            options={
                'db_table': 'produtos_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReceitasMedicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receita', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
                'db_table': 'receitas_medicas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Tipo produto',
                'verbose_name_plural': 'Tipos produto',
                'db_table': 'tipos_produtos',
                'managed': False,
            },
        ),
    ]
