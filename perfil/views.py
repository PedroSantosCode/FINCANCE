from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from .utils import calcula_total, calcula_equilibrio_financeiro
from extrato.models import Valores
from datetime import datetime
from django.db.models import Sum
import json

def home(request):
    from dateutil.relativedelta import relativedelta
    
    valores = Valores.objects.filter(data__month=datetime.now().month)
    entradas = valores.filter(tipo='E')
    saidas = valores.filter(tipo='S')

    total_entradas = calcula_total(entradas, 'valor')
    total_saidas = calcula_total(saidas, 'valor')

    contas = Conta.objects.all()
    total_contas = calcula_total(contas, 'valor')
    
    percentual_gastos_essenciais, percentual_gastos_nao_essenciais = calcula_equilibrio_financeiro()

    # Alertas de orçamento
    categorias_alerta = []
    for cat in Categoria.objects.all():
        if cat.valor_planejamento > 0:
            gasto = cat.total_gasto()
            if gasto > cat.valor_planejamento:
                categorias_alerta.append({
                    'nome': cat.categoria,
                    'gasto': gasto,
                    'limite': cat.valor_planejamento,
                    'excesso': gasto - cat.valor_planejamento,
                })

    # Chart data for home (last 6 months)
    hoje = datetime.now()
    meses_pt = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
                7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}
    
    chart_labels = []
    chart_entradas = []
    chart_saidas = []
    
    for i in range(5, -1, -1):
        data_ref = hoje - relativedelta(months=i)
        mes = data_ref.month
        ano = data_ref.year
        chart_labels.append(f'{meses_pt[mes]}')
        
        e = Valores.objects.filter(tipo='E', data__month=mes, data__year=ano)
        s = Valores.objects.filter(tipo='S', data__month=mes, data__year=ano)
        
        chart_entradas.append(float(sum(v.valor for v in e)))
        chart_saidas.append(float(sum(v.valor for v in s)))

    return render(request, 'home.html', {
        'contas': contas,
        'total_contas': total_contas,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'percentual_gastos_essenciais': int(percentual_gastos_essenciais),
        'percentual_gastos_nao_essenciais': int(percentual_gastos_nao_essenciais),
        'categorias_alerta': categorias_alerta,
        'chart_labels': json.dumps(chart_labels),
        'chart_entradas': json.dumps(chart_entradas),
        'chart_saidas': json.dumps(chart_saidas),
    })

def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    
    total_contas = calcula_total(contas, 'valor')

    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas, 'categorias': categorias})
    
def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/perfil/gerenciar/')
    
    conta = Conta(
        apelido=apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Perfil cadastrado com sucesso')
    return redirect('/perfil/gerenciar/')

def deletar_banco(request, id):
    conta = Conta.objects.get(id=id)
    conta.delete()

    messages.add_message(request, constants.SUCCESS, 'Perfil deletado com sucesso')
    return redirect('/perfil/gerenciar/')

def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
    return redirect('/perfil/gerenciar/')

def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.essencial = not categoria.essencial
    categoria.save()
    return redirect('/perfil/gerenciar/')

def dashboard(request):
    from dateutil.relativedelta import relativedelta

    hoje = datetime.now()
    meses_param = int(request.GET.get('meses', 6))

    # 1. Gastos por categoria (mês atual)
    cat_labels = []
    cat_values = []
    categorias = Categoria.objects.all()
    for categoria in categorias:
        total = 0
        valores = Valores.objects.filter(categoria=categoria, tipo='S', data__month=hoje.month, data__year=hoje.year)
        for v in valores:
            total += v.valor
        if total > 0:
            cat_labels.append(categoria.categoria)
            cat_values.append(float(total))

    # 2. Evolução mensal (últimos N meses)
    evolucao_labels = []
    evolucao_entradas = []
    evolucao_saidas = []

    meses_pt = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
                7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}

    for i in range(meses_param - 1, -1, -1):
        data_ref = hoje - relativedelta(months=i)
        mes = data_ref.month
        ano = data_ref.year
        evolucao_labels.append(f'{meses_pt[mes]}/{ano}')

        entradas = Valores.objects.filter(tipo='E', data__month=mes, data__year=ano)
        saidas = Valores.objects.filter(tipo='S', data__month=mes, data__year=ano)

        total_e = sum(v.valor for v in entradas)
        total_s = sum(v.valor for v in saidas)

        evolucao_entradas.append(float(total_e))
        evolucao_saidas.append(float(total_s))

    # 3. Saldo ao longo do tempo (últimos N meses)
    saldo_labels = []
    saldo_values = []
    saldo_acumulado = 0

    # Calcular saldo inicial (antes do período)
    data_inicio = hoje - relativedelta(months=meses_param)
    valores_anteriores = Valores.objects.filter(data__lt=data_inicio.replace(day=1))
    for v in valores_anteriores:
        if v.tipo == 'E':
            saldo_acumulado += v.valor
        else:
            saldo_acumulado -= v.valor

    for i in range(meses_param - 1, -1, -1):
        data_ref = hoje - relativedelta(months=i)
        mes = data_ref.month
        ano = data_ref.year
        saldo_labels.append(f'{meses_pt[mes]}/{ano}')

        valores_mes = Valores.objects.filter(data__month=mes, data__year=ano)
        for v in valores_mes:
            if v.tipo == 'E':
                saldo_acumulado += v.valor
            else:
                saldo_acumulado -= v.valor

        saldo_values.append(float(saldo_acumulado))

    return render(request, 'dashboard.html', {
        'cat_labels': json.dumps(cat_labels),
        'cat_values': json.dumps(cat_values),
        'evolucao_labels': json.dumps(evolucao_labels),
        'evolucao_entradas': json.dumps(evolucao_entradas),
        'evolucao_saidas': json.dumps(evolucao_saidas),
        'saldo_labels': json.dumps(saldo_labels),
        'saldo_values': json.dumps(saldo_values),
        'meses_param': meses_param,
    })


def api_resumo(request):
    """API endpoint for real-time balance data, notifications, and recent transactions."""
    valores = Valores.objects.filter(data__month=datetime.now().month)
    entradas = valores.filter(tipo='E')
    saidas = valores.filter(tipo='S')

    total_entradas = calcula_total(entradas, 'valor')
    total_saidas = calcula_total(saidas, 'valor')

    contas = Conta.objects.all()
    total_contas = calcula_total(contas, 'valor')

    # Budget alerts
    alertas = []
    for cat in Categoria.objects.all():
        if cat.valor_planejamento > 0:
            gasto = cat.total_gasto()
            if gasto > cat.valor_planejamento:
                alertas.append({
                    'nome': cat.categoria,
                    'gasto': gasto,
                    'limite': cat.valor_planejamento,
                    'excesso': gasto - cat.valor_planejamento,
                })

    # Last 5 transactions
    ultimas = Valores.objects.all().order_by('-data', '-id')[:5]
    ultimas_transacoes = []
    for v in ultimas:
        ultimas_transacoes.append({
            'descricao': v.descricao,
            'valor': float(v.valor),
            'tipo': v.tipo,
            'data': v.data.strftime('%d/%m/%Y') if v.data else '',
            'categoria': str(v.categoria),
            'conta': str(v.conta),
        })

    # Per-account balances
    contas_data = []
    for c in contas:
        contas_data.append({
            'id': c.id,
            'apelido': c.apelido,
            'valor': float(c.valor),
            'tipo': c.get_tipo_display(),
            'perfil': c.get_banco_display(),
        })

    # Recent bill payments
    from contas.models import ContaPaga
    pagamentos_recentes = []
    for p in ContaPaga.objects.select_related('conta', 'conta_bancaria').order_by('-data_pagamento', '-id')[:5]:
        pagamentos_recentes.append({
            'titulo': p.conta.titulo,
            'valor': float(p.valor_pago),
            'data': p.data_pagamento.strftime('%d/%m/%Y') if p.data_pagamento else '',
            'metodo': p.get_metodo_pagamento_display(),
            'conta_bancaria': p.conta_bancaria.apelido if p.conta_bancaria else '',
            'boleto_id': p.id,
        })

    return JsonResponse({
        'total_contas': float(total_contas),
        'total_entradas': float(total_entradas),
        'total_saidas': float(total_saidas),
        'alertas': alertas,
        'ultimas_transacoes': ultimas_transacoes,
        'contas': contas_data,
        'pagamentos_recentes': pagamentos_recentes,
    })


def calculadora(request):
    return render(request, 'calculadora.html')


def landing_page(request):
    from blog.models import BlogPost
    latest_posts = BlogPost.objects.filter(published=True)[:3]
    return render(request, 'landing.html', {'latest_posts': latest_posts})
