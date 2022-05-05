from django.db import models
import uuid

# Create your models here.

class Expenditure(models.Model):
    STATUS_CHOICES = (
        ('not_sended', 'Aguardando Envio'),
        ('disapproved', 'Reprovado'),
        ('waiting', 'Aguardando aprovação'),
        ('approved', 'Aprovado'),
        ('expired', 'Vencido'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="Registro ativo?")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Status atual')
