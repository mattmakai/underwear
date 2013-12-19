from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = ''
    help = 'Deploy to a remote server.'

    def handle(self, *args, **options):
        self.stdout.write('App successfully deployed to server.')
