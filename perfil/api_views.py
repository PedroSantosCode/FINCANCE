from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .categoria_rules import sugerir_categoria

@csrf_exempt
def sugerir_categoria_view(request):
    descricao = request.GET.get('descricao', '')
    
    resultado = sugerir_categoria(descricao)
    
    if resultado:
        return JsonResponse({
            'encontrado': True,
            'categoria_id': resultado['id'],
            'categoria_nome': resultado['nome'],
            'confianca': resultado['confianca'],
            'motivo': resultado['motivo'],
        })
    
    return JsonResponse({'encontrado': False})
