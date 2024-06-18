from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run database migrations'

    def handle(self, *args, **kwargs):
        call_command('makemigrations')
        call_command('migrate')