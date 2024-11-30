from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

from products.models import populate, Product

class Command(BaseCommand):
    help = 'Popola il database con un insieme di prodotti demo'

    def handle(self, *args, **kwargs):
        if Product.objects.exists():
            self.stdout.write(self.style.WARNING('database già popolato con i prodotti demo'))
        else:
            self.stdout.write(self.style.SUCCESS('popolando il database con prodotti demo...'))
            populate()
            self.stdout.write(self.style.SUCCESS('database popolato con successo'))
            
        

