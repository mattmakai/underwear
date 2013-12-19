from django.core.management.base import BaseCommand, CommandError

from underwear.run_underwear import deploy

class Command(BaseCommand):
    args = '/etc/ansible/hosts'
    help = 'Deploy to a remote server.'

    def handle(self, *args, **options):
        print args
        print args[0]
        deploy(['django-stack.yml', '-i', args[1]])
        self.stdout.write('App successfully deployed to server.')
