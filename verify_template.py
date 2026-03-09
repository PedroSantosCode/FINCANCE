import os
import django
from django.template.loader import render_to_string
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Mock context
class MockObj:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

conta_pagar = MockObj(titulo='Test', categoria='Test', descricao='Desc', dia_pagamento=10, recorrente=True, valor=100)

context = {
    'conta_pagar': conta_pagar,
    'contas_bancarias': [],
    'ja_paga': False,
    'messages': []
}

try:
    html = render_to_string('pagar_conta.html', context)
    print("Template rendered successfully!")
except Exception as e:
    print(f"Error: {e}")
