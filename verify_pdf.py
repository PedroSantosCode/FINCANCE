import os
import django
from django.test import RequestFactory
from django.conf import settings
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from contas.views import gerar_boleto
from contas.models import ContaPagar, ContaPaga
from perfil.models import Conta, Categoria

# Ensure dummy data
cat, _ = Categoria.objects.get_or_create(categoria='Teste', defaults={'valor_planejamento': 1000})
conta, _ = Conta.objects.get_or_create(apelido='Conta Teste', defaults={'banco':'PS', 'tipo':'pf', 'valor':5000, 'icone':'icones/default.png'})
cp, _ = ContaPagar.objects.get_or_create(titulo='Conta Teste', defaults={'categoria':cat, 'descricao':'Desc', 'valor':100, 'dia_pagamento':10})

pagamento, _ = ContaPaga.objects.get_or_create(
    conta=cp,
    defaults={
        'conta_bancaria': conta,
        'data_pagamento': datetime.now().date(),
        'valor_pago': 100,
        'metodo_pagamento': 'boleto'
    }
)

factory = RequestFactory()
request = factory.get(f'/contas/boleto/{pagamento.id}/')
# Add necessary middleware/message storage mock if needed, but views usually require messages framework
from django.contrib.messages.storage.fallback import FallbackStorage
setattr(request, 'session', 'session')
setattr(request, '_messages', FallbackStorage(request))


response = gerar_boleto(request, pagamento.id)

print(f"Content-Type: {response['Content-Type']}")
print(f"Content Length: {len(response.content)}")
