from django.shortcuts import render, redirect
from perfil.models import Categoria, Conta
from django.http import HttpResponse, FileResponse
from .models import Valores
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime
from django.template.loader import render_to_string
import os
from django.conf import settings
from weasyprint import HTML 
from io import BytesIO

def novo_valor(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    elif request.method == 'POST':
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo') 


        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo,
        )
 
        valores.save()

        conta = Conta.objects.get(id=conta)

        if tipo == 'E':
            conta.valor += float(valor)
        else:
            conta.valor -= float(valor)

        conta.save()
        
        # Verificar alerta de orçamento
        if tipo == 'S':
            cat_obj = Categoria.objects.get(id=categoria)
            if cat_obj.valor_planejamento > 0:
                gasto_total = cat_obj.total_gasto()
                if gasto_total > cat_obj.valor_planejamento:
                    excesso = gasto_total - cat_obj.valor_planejamento
                    messages.add_message(request, constants.WARNING, 
                        f'⚠️ Orçamento ultrapassado em "{cat_obj.categoria}"! '
                        f'Gasto: R$ {gasto_total:.2f} / Limite: R$ {cat_obj.valor_planejamento:.2f} '
                        f'(Excesso: R$ {excesso:.2f})')

        messages.add_message(request, constants.SUCCESS, 'Entrada/Saída cadastrada com sucesso')
        return redirect('/extrato/novo_valor/')



def view_extrato(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()

    conta_get = request.GET.get('conta')
    categoria_get = request.GET.get('categoria')
    busca = request.GET.get('busca', '').strip()

    valores = Valores.objects.filter(data__month=datetime.now().month)
    
    if busca:
        valores = valores.filter(descricao__icontains=busca)
    
    if conta_get:
        valores = valores.filter(conta__id=conta_get)

    if categoria_get:
        valores = valores.filter(categoria__id=categoria_get)
    
    # Calculate totals for the filtered results
    total_entradas = sum(v.valor for v in valores.filter(tipo='E'))
    total_saidas = sum(v.valor for v in valores.filter(tipo='S'))
    saldo = total_entradas - total_saidas
    
    return render(request, 'view_extrato.html', {
        'valores': valores,
        'contas': contas,
        'categorias': categorias,
        'busca': busca,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'saldo': saldo,
    })




def exportar_pdf(request):
    valores = Valores.objects.filter(data__month=datetime.now().month)

    total_entradas = sum(v.valor for v in valores.filter(tipo='E'))
    total_saidas = sum(v.valor for v in valores.filter(tipo='S'))
    saldo = total_entradas - total_saidas

    template_render = render_to_string('partials/extrato.html', {
        'valores': valores,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'saldo': saldo,
    })
    path_output = BytesIO()

    HTML(string=template_render).write_pdf(path_output)

    path_output.seek(0)

    return FileResponse(path_output, filename="extrato.pdf") 