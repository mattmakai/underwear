from django.core.management.base import BaseCommand, CommandError

from underwear.run_underwear import deploy

class Command(BaseCommand):
    args = '[hosts file location]'
    help = 'Deploy to a remote server.'

    def handle(self, *args, **options):
        if len(args) < 1:
            print "Usage: manage.py deploy [hosts file location]\n"
        else:
            deploy(['../../django-stack.yml', '-i', args[0]])
            self.stdout.write('App successfully deployed to server.')
