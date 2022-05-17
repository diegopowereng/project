# Generated by Django 3.2.3 on 2022-05-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenditures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenditure',
            name='status',
        ),
        migrations.AddField(
            model_name='expenditure',
            name='expenditure_type',
            field=models.CharField(choices=[('mercadoria', 'Mercadoria'), ('embalagens', 'Embalagens'), ('despesa_fixa', 'Despesa Fixa'), ('despesa_variavel', 'Despesa Variável'), ('folha_gestão', 'Folha Gestão'), ('folha_operação', 'Folha Operação'), ('investimento', 'Investimento'), ('melhoria_manutencao', 'Melhoria e Manutenção')], default='mercadoria', max_length=20, verbose_name='Tipo da Despesa'),
        ),
        migrations.AddField(
            model_name='expenditure',
            name='obs',
            field=models.CharField(default='obs', max_length=200, verbose_name='Informações da Despesa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expenditure',
            name='payment',
            field=models.CharField(choices=[('pix', 'PIX'), ('boleto', 'Boleto'), ('dinheiro', 'Diinheiro'), ('credito', 'Cartão de Crédito'), ('debito', 'Débito')], default='pix', max_length=20, verbose_name='Forma de Pagamento'),
        ),
    ]