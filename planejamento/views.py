from django.shortcuts import render, redirect
from perfil.models import Categoria
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.messages import constants
from .models import MetaFinanceira
import json

def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor =json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()
    return JsonResponse({'status': 'Sucesso!'})


def ver_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'ver_planejamento.html', {'categorias': categorias})

def metas(request):
    metas_lista = MetaFinanceira.objects.all()
    metas_com_progresso = []
    for meta in metas_lista:
        percentual, valor_atual = meta.calcular_progresso()
        metas_com_progresso.append({
            'meta': meta,
            'percentual': percentual,
            'valor_atual': valor_atual,
            'atingida': percentual >= 100 if meta.tipo == 'economia_mensal' else percentual < 100,
        })
    
    categorias = Categoria.objects.all()
    return render(request, 'metas.html', {'metas': metas_com_progresso, 'categorias': categorias})

def criar_meta(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        tipo = request.POST.get('tipo')
        valor = request.POST.get('valor')
        categoria_id = request.POST.get('categoria')

        meta = MetaFinanceira(
            titulo=titulo,
            tipo=tipo,
            valor=valor,
        )

        if tipo == 'limite_categoria' and categoria_id:
            meta.categoria_id = categoria_id

        meta.save()
        messages.add_message(request, constants.SUCCESS, 'Meta criada com sucesso!')
        return redirect('/planejamento/metas/')

def deletar_meta(request, id):
    meta = MetaFinanceira.objects.get(id=id)
    meta.delete()
    messages.add_message(request, constants.SUCCESS, 'Meta deletada com sucesso!')
    return redirect('/planejamento/metas/')
