from django.db import models
from perfil.models import Categoria, Conta
import random
import string

class ContaPagar(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    valor = models.FloatField()
    dia_pagamento = models.IntegerField()
    recorrente = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

class ContaPaga(models.Model):
    METODO_CHOICES = (
        ('boleto', 'Boleto Bancário'),
        ('pix', 'PIX'),
        ('debito', 'Débito Automático'),
        ('transferencia', 'Transferência'),
    )

    conta = models.ForeignKey(ContaPagar, on_delete=models.DO_NOTHING)
    conta_bancaria = models.ForeignKey(Conta, on_delete=models.SET_NULL, null=True, blank=True)
    data_pagamento = models.DateField()
    valor_pago = models.FloatField(default=0)
    metodo_pagamento = models.CharField(max_length=20, choices=METODO_CHOICES, default='boleto')
    codigo_barras = models.CharField(max_length=60, blank=True)
    nosso_numero = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        if not self.codigo_barras:
            self.codigo_barras = ''.join(random.choices(string.digits, k=47))
        if not self.nosso_numero:
            self.nosso_numero = ''.join(random.choices(string.digits, k=10))
        if not self.valor_pago:
            self.valor_pago = self.conta.valor
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.conta.titulo} — {self.data_pagamento}'