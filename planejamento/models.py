from django.db import models
from datetime import datetime
from perfil.models import Categoria

class MetaFinanceira(models.Model):
    tipo_choices = (
        ('economia_mensal', 'Economizar por mês'),
        ('limite_categoria', 'Limite de gasto por categoria'),
    )

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=tipo_choices)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def calcular_progresso(self):
        from extrato.models import Valores
        mes_atual = datetime.now().month
        ano_atual = datetime.now().year

        if self.tipo == 'economia_mensal':
            entradas = Valores.objects.filter(tipo='E', data__month=mes_atual, data__year=ano_atual)
            saidas = Valores.objects.filter(tipo='S', data__month=mes_atual, data__year=ano_atual)
            total_entradas = sum(v.valor for v in entradas)
            total_saidas = sum(v.valor for v in saidas)
            economizado = total_entradas - total_saidas
            if self.valor > 0:
                percentual = min(int((economizado / self.valor) * 100), 100)
                return max(percentual, 0), economizado
            return 0, economizado

        elif self.tipo == 'limite_categoria' and self.categoria:
            gasto = self.categoria.total_gasto()
            if self.valor > 0:
                percentual = min(int((gasto / self.valor) * 100), 100)
                return percentual, gasto
            return 0, gasto

        return 0, 0
