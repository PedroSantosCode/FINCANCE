from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create admin superuser with admin/admin credentials'

    def handle(self, *args, **options):
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.WARNING('Admin user already exists. Skipping.'))
            return

        User.objects.create_superuser(
            username='admin',
            email='admin@finance.bank',
            password='admin',
        )
        self.stdout.write(self.style.SUCCESS('Created admin superuser (admin/admin)'))
