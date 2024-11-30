from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from accounts.models import Account, Supervisor

class Command(BaseCommand):
    help = "Crea un account supervisore demo"

    def handle(self, *args, **kwargs):
        
        supervisor_group= Group.objects.filter(name='supervisors').first()
        if supervisor_group is None:
            self.stdout.write(self.style.ERROR('gruppo "supervisors" non esistente, hai eseguito prima "python manage.py creategroups"?'))
            return



        account = Account.objects.filter(username='supervisorDemo').first()
        if account is None:
            account = Account.objects.create_user(
                username='supervisorDemo',
                password='supervisorDemo',
                email='supervisorDemo@example.com',
                age=30
            )
            self.stdout.write(self.style.SUCCESS(f'account "{account.username}" (con password "{account.username}") creato con successo'))
        else:
            self.stdout.write(self.style.WARNING(f'account "{account.username}" (con password "{account.username}") già esistente'))

        account.groups.add(supervisor_group)

        supervisor, created = Supervisor.objects.get_or_create(account=account)
        if created:
            self.stdout.write(self.style.SUCCESS(f'l\'account "{account.username}" è stato abilitato ad essere un supervisore'))
        else:
            self.stdout.write(self.style.WARNING(f'l\'account "{account.username}" è già abilitato ad essere un supervisore'))
