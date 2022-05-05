# Generated by Django 3.2.3 on 2022-05-05 22:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Registro ativo?')),
                ('status', models.CharField(choices=[('not_sended', 'Aguardando Envio'), ('disapproved', 'Reprovado'), ('waiting', 'Aguardando aprovação'), ('approved', 'Aprovado'), ('expired', 'Vencido')], default='not_sended', max_length=20, verbose_name='Status atual')),
            ],
        ),
    ]