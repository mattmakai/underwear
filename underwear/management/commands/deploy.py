from django.core.management.base import BaseCommand, CommandError

from underwear.run_underwear import deploy

class Command(BaseCommand):
    args = '[hosts file location] [private key path and filename] [custom' + \
        ' app variables]'
    help = 'Deploy to one or more remote servers.'

    def handle(self, *args, **options):
        if len(args) < 3:
            deploy(['django-stack.yml', '-i', './deploy/hosts', '-K', '-u', 
                'deployer', '--private-key=%s' % './deploy/ssh_conf/id_rsa', 
                '--extra-vars', '@%s' % './deploy/underwear.yml'])
        else:
            deploy(['django-stack.yml', '-i', args[0], '-K', '-u', 
                'deployer', '--private-key=%s' % args[1], 
                '--extra-vars', '@%s' % args[2]])
