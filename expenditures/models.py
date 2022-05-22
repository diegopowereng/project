import datetime
from django.db import models
import uuid
from django.utils import timezone

# Create) your models here.

class Expenditure(models.Model):
    RESPONSIBLE_CHOICES = (
        ('JESSICA', 'JESSICA'),
        ('DIEGO', 'DIEGO'),
        ('TATHI', 'TATHI'),
    )
    PAYMENT_CHOICES = (
        ('pix', 'PIX'),
        ('boleto', 'Boleto'),
        ('dinheiro', 'Diinheiro'),
        ('credito', 'Cartão de Crédito'),
        ('debito', 'Débito'),
    )
    TYPE_CHOICES = (
        ('mercadoria', 'Mercadoria'),
        ('embalagens', 'Embalagens'),
        ('revenda', 'Revenda'),
        ('despesa_fixa', 'Despesa Fixa'),
        ('despesa_variavel', 'Despesa Variável'),
        ('folha_gestão', 'Folha Gestão'),
        ('folha_operação', 'Folha Operação'),
        ('investimento', 'Investimento'),
        ('melhoria_manutencao', 'Melhoria e Manutenção')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    created_at = models.DateField(default=datetime.date.today)
    scheduled = models.BooleanField(default=False, verbose_name="Agendado?")
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default=PAYMENT_CHOICES[0][0], verbose_name='Forma de Pagamento')
    expenditure_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0], verbose_name='Tipo da Despesa')
    obs = models.CharField(max_length=200, verbose_name='Informações da Despesa')
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    receipt = models.FileField(verbose_name="Comprovante", upload_to='comprovantes', blank=True, null=True)
    scheduled_date =  models.DateField(blank=True, null=True)
    responsible = models.CharField(max_length=20, choices=RESPONSIBLE_CHOICES, default=RESPONSIBLE_CHOICES[0][0], verbose_name='Responsável')


    class Meta:
        verbose_name_plural = "despesas"
        verbose_name = "despesa"


    def __str__(self,):
        return str(self.created_at) + ' - ' + str(self.amount) + ' - ' + str(self.scheduled)
