from django.core.management.base import BaseCommand, CommandError

from underwear.run_underwear import deploy

class Command(BaseCommand):
    args = '[hosts file location] [private key path and filename] [custom' + \
        ' app variables]'
    help = 'Deploy to one or more remote servers.'

    def handle(self, *args, **options):
        if len(args) < 3:
            print "Usage: manage.py deploy [hosts file location] " + \
                "[private key path and filename] [custom app variables]\n"
        else:
            print 'args[2]: %s' % args[2]
            deploy(['django-stack.yml', '-i', args[0], '-K', '-u', 
                'deployer', '--private-key=%s' % args[1], 
                '--extra-vars', '"@%s"' % args[2]])
            self.stdout.write('App successfully deployed to server.')
