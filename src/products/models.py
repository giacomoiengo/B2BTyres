from ast import pattern
import string
import os.path
from django.db import models
from accounts.models import Customer
import csv
from .utils import percentage



class Product(models.Model):
    article = models.CharField(help_text='Articolo', primary_key=True, max_length=20, null=False, blank=False)
    brand = models.CharField(help_text='Marca', max_length=30, null=False, blank=False)
    width = models.PositiveSmallIntegerField(help_text='Larghezza', null=False, blank=False)
    height = models.PositiveSmallIntegerField(help_text='Altezza', null=False, blank=False)
    speed = models.CharField(help_text='Velocita', max_length=2, null=True, blank=True)
    rim = models.PositiveSmallIntegerField(help_text='Rim', null=False, blank=False)
    load_index = models.CharField(help_text='Indice di carico', max_length=20, null=False, blank=False)
    pattern = models.CharField(help_text='Pattern', max_length=70, null=False, blank=False)
    # [Spec]
    pr_rf = models.CharField(help_text='Pr/Rf', max_length=8, null=True, blank=True)
    # [Demo]
    # [Dot]
    # [Extra]
    quality = models.CharField(help_text='Classe', max_length=20, null=False, blank=False)
    vehicle = models.CharField(help_text='Veicolo', max_length=25, null=False, blank=False)
    stock = models.PositiveSmallIntegerField(help_text='Disponibili', null=False, blank=False)
    price = models.FloatField(help_text='Prezzo', null=False, blank=False)
    discount = models.FloatField(help_text='Sconto', null=False, blank=False)
    ean = models.CharField(help_text='Numero di articolo europeo', max_length=25, null=True, blank=True)
    ip_code = models.CharField(help_text='Codice ip', max_length=30, null=True, blank=True)
    fuel = models.CharField(help_text='Efficienza dei consumi', max_length=1, null=True, blank=True)
    wet = models.CharField(help_text='Aderenza sul bagnato', max_length=1, null=True, blank=True)
    noise = models.CharField(help_text='Rumorosita\'', max_length=1, null=True, blank=True)
    decibel = models.PositiveSmallIntegerField(help_text='Decibel', null=False, blank=False)
    c_class = models.CharField(help_text='Classe C', max_length=2, null=False, blank=False)
    url_pattern = models.URLField(help_text='Link foto', max_length=200, null=True, blank=True)
    # [Per parcel]
    # [RFT]
    eprel_code = models.PositiveIntegerField(help_text='Etichetta europea', null=True, blank=True)
    eprel_rr = models.CharField(help_text='Eprel rr', max_length=1, null=True, blank=True)
    eprel_wet = models.CharField(help_text='Eprel wet', max_length=1, null=True, blank=True)
    eprel_noise = models.CharField(help_text='Eprel noise', max_length=1, null=True, blank=True)
    eprel_decibel = models.PositiveSmallIntegerField(help_text='Eprel decibel', null=True, blank=True)
    eprel_severe_snow = models.PositiveSmallIntegerField(help_text='Eprel severe snow', null=False, blank=False)
    eprel_ice_tyre = models.PositiveSmallIntegerField(help_text='Eprel ice tyre', null=False, blank=False)

    def adjust_price(self, customer:Customer):
        # FIXME markup and discount are integers
        return round((
                self.price + 
                percentage(float(customer.markup), self.price) -
                percentage(float(customer.discount), self.price)
            ),
            2
        )

    def generate_schema(self):
        schema = {}
        for field in filter(lambda f: not f.is_relation, self._meta.get_fields()):
            if type(field) in [models.CharField, models.URLField]:
                schema[field.name] = {
                    'type':'string',
                    'maxLength': field.max_length
                }

            elif type(field) in [models.PositiveSmallIntegerField, models.PositiveIntegerField]:
                schema[field.name] = {
                    'type':'string',
                    'pattern':'^[0-9]+$'
                }




def populate():
    filename = os.path.join('products', 'CSV', 'product-demo.csv')
    dicts = []
    with open(filename, 'r', newline='') as f:
        for dict_ in csv.DictReader(f, delimiter=';', fieldnames=None, restkey=None, restval=None):
            dicts.append(dict_)

    
    for entry in dicts:
        product = Product(
            article=entry['Article'],
            brand=entry['Brand'],
            width=int(entry['Width']),
            height=int(entry['Height']),
            speed=entry['Speed'],
            rim=int(entry['Rim']),
            load_index=entry['Loadindex'],
            pattern=entry['Pattern'],
            # spec=entry['Spec'],
            pr_rf=entry['PR/RF'],
            # demo=entry['Demo'],
            # dot=entry['Dot'],
            # extra=entry['Extra'],
            quality=entry['Quality'],
            vehicle=entry['Vehicle'],
            stock=int(entry['Stock']),
            price=float(entry['Price']),
            discount=float(entry['Discount']),
            ean=entry['EAN'],
            ip_code=entry['IPCODE'],
            fuel=entry['Fuel'],
            wet=entry['Wet'],
            noise=entry['Noise'],
            decibel=int(entry['Decibel']),
            c_class=entry['C Class'],
            url_pattern=entry['URL_Pattern'],
            # per parcel=entry['Per parcel'],
            # rft=entry['RFT'],
            eprel_code=None if entry['Eprel_code'] == '' else int(entry['Eprel_code']),
            eprel_rr=entry['Eprel_RR'],
            eprel_wet=entry['Eprel_Wet'],
            eprel_noise=entry['Eprel_Noise'],
            eprel_decibel=None if entry['Eprel_decibel'] == '' else int(entry['Eprel_decibel']),
            eprel_severe_snow=int(entry['Eprel_severe_snow']),
            eprel_ice_tyre=int(entry['Eprel_Ice_Tyre']),
        
        )
        product.save()