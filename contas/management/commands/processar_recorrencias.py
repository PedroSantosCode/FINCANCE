from django.core.management.base import BaseCommand
from contas.models import ContaPagar, ContaPaga
from extrato.models import Valores
from perfil.models import Conta
from datetime import datetime, date

class Command(BaseCommand):
    help = 'Processa despesas recorrentes e cria lançamentos automáticos'

    def handle(self, *args, **options):
        hoje = date.today()
        mes_atual = hoje.month
        ano_atual = hoje.year
        dia_atual = hoje.day

        contas_recorrentes = ContaPagar.objects.filter(recorrente=True)
        
        criados = 0
        for conta in contas_recorrentes:
            # Verificar se já foi paga ou processada este mês
            ja_paga = ContaPaga.objects.filter(
                conta=conta,
                data_pagamento__month=mes_atual,
                data_pagamento__year=ano_atual,
            ).exists()

            if not ja_paga and conta.dia_pagamento <= dia_atual:
                # Pegar a primeira conta bancária disponível
                conta_bancaria = Conta.objects.first()
                if conta_bancaria:
                    # Criar o valor como saída
                    Valores.objects.create(
                        valor=conta.valor,
                        categoria=conta.categoria,
                        descricao=f'[Recorrente] {conta.titulo} - {conta.descricao}',
                        data=date(ano_atual, mes_atual, conta.dia_pagamento),
                        conta=conta_bancaria,
                        tipo='S',
                    )

                    # Marcar como paga
                    ContaPaga.objects.create(
                        conta=conta,
                        data_pagamento=hoje,
                    )

                    # Atualizar saldo da conta
                    conta_bancaria.valor -= conta.valor
                    conta_bancaria.save()

                    criados += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'Processada: {conta.titulo} - R$ {conta.valor}')
                    )

        self.stdout.write(
            self.style.SUCCESS(f'\nTotal de recorrências processadas: {criados}')
        )
