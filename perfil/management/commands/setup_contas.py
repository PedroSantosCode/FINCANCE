import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from perfil.models import Conta


class Command(BaseCommand):
    help = 'Popula o banco com 11 contas bancárias associadas às imagens do mediaimages'

    def handle(self, *args, **options):
        contas_data = [
            {'apelido': 'Conta Principal', 'banco': 'NU', 'tipo': 'pf', 'valor': 15420.50, 'img': '1.png'},
            {'apelido': 'Reserva de Emergência', 'banco': 'CE', 'tipo': 'pf', 'valor': 32800.00, 'img': '2.png'},
            {'apelido': 'Investimentos', 'banco': 'IT', 'tipo': 'pf', 'valor': 87650.75, 'img': '3.png'},
            {'apelido': 'Empresarial', 'banco': 'BR', 'tipo': 'pj', 'valor': 45200.00, 'img': '4.png'},
            {'apelido': 'Poupança', 'banco': 'BB', 'tipo': 'pf', 'valor': 12300.00, 'img': '5.png'},
            {'apelido': 'Salário', 'banco': 'SA', 'tipo': 'pf', 'valor': 8750.30, 'img': '6.png'},
            {'apelido': 'Digital', 'banco': 'IN', 'tipo': 'pf', 'valor': 5430.00, 'img': '7.png'},
            {'apelido': 'C6 Premium', 'banco': 'C6', 'tipo': 'pf', 'valor': 21000.00, 'img': '8.png'},
            {'apelido': 'BTG Wealth', 'banco': 'BT', 'tipo': 'pf', 'valor': 150320.00, 'img': '9.png'},
            {'apelido': 'XP Carteira', 'banco': 'XP', 'tipo': 'pf', 'valor': 67800.00, 'img': '10.png'},
            {'apelido': 'Safra Private', 'banco': 'SF', 'tipo': 'pf', 'valor': 234212.00, 'img': '11.png'},
        ]

        source_dir = os.path.join(settings.MEDIA_ROOT, 'icones', 'mediaimages')
        dest_dir = os.path.join(settings.MEDIA_ROOT, 'icones')

        # Also copy Logo.png and bg.png
        for asset in ['Logo.png', 'bg.png']:
            src = os.path.join(source_dir, asset)
            dst = os.path.join(dest_dir, asset)
            if os.path.exists(src):
                shutil.copy2(src, dst)
                self.stdout.write(f'  Copiado {asset}')

        # Clear existing contas (and related Valores to avoid FK constraint)
        from extrato.models import Valores
        Valores.objects.all().delete()
        Conta.objects.all().delete()
        self.stdout.write(self.style.WARNING('Contas e valores existentes removidos.'))

        for data in contas_data:
            img_src = os.path.join(source_dir, data['img'])
            img_dst = os.path.join(dest_dir, data['img'])

            if os.path.exists(img_src):
                shutil.copy2(img_src, img_dst)

            conta = Conta(
                apelido=data['apelido'],
                banco=data['banco'],
                tipo=data['tipo'],
                valor=data['valor'],
                icone=f"icones/{data['img']}",
            )
            conta.save()
            self.stdout.write(self.style.SUCCESS(f'  [OK] {data["apelido"]} ({data["banco"]}) - {data["img"]}'))

        self.stdout.write(self.style.SUCCESS(f'\n[DONE] {len(contas_data)} contas criadas com sucesso!'))
