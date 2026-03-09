import urllib.request
import sys

pages = [
    '/',
    '/perfil/home/',
    '/perfil/gerenciar/',
    '/extrato/novo_valor/',
    '/extrato/view_extrato/',
    '/perfil/dashboard/',
    '/contas/definir_contas/',
    '/contas/ver_contas/',
    '/planejamento/ver_planejamento/',
    '/planejamento/metas/',
    '/planejamento/definir_planejamento/',
    '/blog/',
]

all_ok = True
for p in pages:
    try:
        r = urllib.request.urlopen('http://localhost:8000' + p)
        html = r.read().decode('utf-8')
        has_sidebar = 'sidebar' in html
        has_glass = 'glass-card' in html
        print(f'  [OK] {p} -> {r.status} (sidebar={has_sidebar}, glass={has_glass}, len={len(html)})')
    except Exception as e:
        print(f'  [FAIL] {p} -> {e}')
        all_ok = False

if all_ok:
    print('\n[DONE] All pages OK!')
else:
    print('\n[ERROR] Some pages failed!')
    sys.exit(1)
