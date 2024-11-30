from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group



class Command(BaseCommand):
    help = "Crea gruppi per il funzionamento dell'app"

    def handle(self, *args, **kwargs):
        
        supervisor_group, created = Group.objects.get_or_create(name='supervisors')
        if created:
            self.stdout.write(self.style.SUCCESS('gruppo "supervisors" creato con successo'))
        else:
            self.stdout.write(self.style.WARNING('gruppo "supervisors" già esistente'))

        salesman_group, created = Group.objects.get_or_create(name='salesmen')
        if created:
            self.stdout.write(self.style.SUCCESS('gruppo "salesmen" creato con successo'))
        else:
            self.stdout.write(self.style.WARNING('gruppo "salesmen" già esistente'))

        customer_group, created = Group.objects.get_or_create(name='customers')
        if created:
            self.stdout.write(self.style.SUCCESS('gruppo "customers" creato con successo'))
        else:
            self.stdout.write(self.style.WARNING('gruppo "salesmen" già esistente'))