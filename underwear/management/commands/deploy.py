from django.core.management.base import BaseCommand, CommandError

from underwear.run_underwear import deploy

class Command(BaseCommand):
    args = '[hosts file location] [private key path and filename]'
    help = 'Deploy to a remote server.'

    def handle(self, *args, **options):
        if len(args) < 2:
            print "Usage: manage.py deploy [hosts file location] " + \
                "[private key path and filename]\n"
        else:
            deploy(['django-stack.yml', '-i', args[0], '-K', '-u', 
                'deployer', '--private-key=%s' % args[1]])
            self.stdout.write('App successfully deployed to server.')
