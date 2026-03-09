from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from perfil.models import Categoria, Conta
from extrato.models import Valores
from .models import ContaPagar, ContaPaga
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

def definir_contas(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'definir_contas.html', {'categorias': categorias})
    else:
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        dia_pagamento = request.POST.get('dia_pagamento')
        recorrente = bool(request.POST.get('recorrente'))

        conta = ContaPagar(
            titulo=titulo,
            categoria_id=categoria,
            descricao=descricao,
            valor=valor,
            dia_pagamento=dia_pagamento,
            recorrente=recorrente,
        )

        conta.save()

        messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso!')
        return redirect('/contas/definir_contas/')
    

def ver_contas(request):
    MES_ATUAL = datetime.now().month
    DIA_ATUAL = datetime.now().day

    contas = ContaPagar.objects.all()

    contas_pagas = ContaPaga.objects.filter(data_pagamento__month=MES_ATUAL).values('conta')
    
    contas_vencidas = contas.filter(dia_pagamento__lt=DIA_ATUAL).exclude(id__in=contas_pagas)
    
    contas_proximas_vencimento = contas.filter(dia_pagamento__lte=DIA_ATUAL + 5).filter(dia_pagamento__gt=DIA_ATUAL).exclude(id__in=contas_pagas)

    restantes = contas.exclude(id__in=contas_vencidas).exclude(id__in=contas_proximas_vencimento).exclude(id__in=contas_pagas)

    # Get paid bills for this month with their payment details
    pagamentos_mes = ContaPaga.objects.filter(
        data_pagamento__month=MES_ATUAL
    ).select_related('conta', 'conta_bancaria').order_by('-data_pagamento', '-id')

    return render(request, 'ver_contas.html', {
        'contas_vencidas': contas_vencidas,
        'contas_proximas_vencimento': contas_proximas_vencimento,
        'restantes': restantes,
        'pagamentos_mes': pagamentos_mes,
    })


def pagar_conta(request, id):
    conta_pagar = get_object_or_404(ContaPagar, id=id)
    contas_bancarias = Conta.objects.all()

    # Check if already paid this month
    mes_atual = datetime.now().month
    ja_paga = ContaPaga.objects.filter(conta=conta_pagar, data_pagamento__month=mes_atual).exists()

    if request.method == 'GET':
        return render(request, 'pagar_conta.html', {
            'conta_pagar': conta_pagar,
            'contas_bancarias': contas_bancarias,
            'metodos': ContaPaga.METODO_CHOICES,
            'ja_paga': ja_paga,
        })

    # POST — process payment
    if ja_paga:
        messages.add_message(request, constants.WARNING,
                             f'A conta "{conta_pagar.titulo}" já foi paga este mês.')
        return redirect('ver_contas')

    conta_bancaria_id = request.POST.get('conta_bancaria')
    metodo = request.POST.get('metodo_pagamento', 'boleto')

    if not conta_bancaria_id:
        messages.add_message(request, constants.ERROR, 'Selecione uma conta bancária para pagamento.')
        return redirect('pagar_conta', id=id)

    conta_bancaria = get_object_or_404(Conta, id=conta_bancaria_id)

    # Check sufficient balance
    if conta_bancaria.valor < conta_pagar.valor:
        messages.add_message(request, constants.ERROR,
                             f'Saldo insuficiente na conta "{conta_bancaria.apelido}". '
                             f'Saldo: R$ {conta_bancaria.valor:.2f} / Valor: R$ {conta_pagar.valor:.2f}')
        return redirect('pagar_conta', id=id)

    # 1. Create ContaPaga record
    pagamento = ContaPaga.objects.create(
        conta=conta_pagar,
        conta_bancaria=conta_bancaria,
        data_pagamento=datetime.now().date(),
        valor_pago=conta_pagar.valor,
        metodo_pagamento=metodo,
    )

    # 2. Create Valores entry (Saída) for dashboard integration
    Valores.objects.create(
        valor=conta_pagar.valor,
        categoria=conta_pagar.categoria,
        descricao=f'Pagamento: {conta_pagar.titulo}',
        data=datetime.now().date(),
        conta=conta_bancaria,
        tipo='S',
    )

    # 3. Subtract from the bank account balance
    conta_bancaria.valor -= conta_pagar.valor
    conta_bancaria.save()

    messages.add_message(request, constants.SUCCESS,
                         f'✅ Conta "{conta_pagar.titulo}" paga com sucesso via {pagamento.get_metodo_pagamento_display()}! '
                         f'Valor: R$ {conta_pagar.valor:.2f} debitado de "{conta_bancaria.apelido}".')
    return redirect('ver_contas')


def gerar_boleto(request, id):
    """Generate a fictitious boleto bancário PDF for a paid bill."""
    pagamento = get_object_or_404(ContaPaga, id=id)
    conta_pagar = pagamento.conta

    # Format barcode with dots for readability
    cb = pagamento.codigo_barras
    codigo_formatado = f'{cb[:5]}.{cb[5:10]} {cb[10:15]}.{cb[15:21]} {cb[21:26]}.{cb[26:32]} {cb[32]} {cb[33:47]}'

    context = {
        'pagamento': pagamento,
        'conta_pagar': conta_pagar,
        'codigo_formatado': codigo_formatado,
        'banco_nome': pagamento.conta_bancaria.apelido if pagamento.conta_bancaria else 'Finance.Bank',
        'banco_perfil': pagamento.conta_bancaria.get_banco_display() if pagamento.conta_bancaria else '',
        'data_vencimento': f'{conta_pagar.dia_pagamento:02d}/{datetime.now().month:02d}/{datetime.now().year}',
        'data_pagamento': pagamento.data_pagamento.strftime('%d/%m/%Y'),
        'now': datetime.now(),
    }

    html_string = render_to_string('boleto_template.html', context)

    try:
        from weasyprint import HTML
        pdf = HTML(string=html_string).write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="boleto_{pagamento.nosso_numero}.pdf"'
        return response
    except ImportError:
        # Fallback: return HTML version
        return HttpResponse(html_string, content_type='text/html')