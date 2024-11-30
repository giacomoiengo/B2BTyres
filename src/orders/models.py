from django.db import models
from accounts.models import Customer
from products.models import Product



class Order(models.Model):
    # ORDER_STATUS_CHOICES = (
    #     ('created', 'Created'),
    #     ('paid', 'Paid'),
    #     ('shipped', 'Shipped'),
    #     ('refunded', 'Refunded'),
    # )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    products = models.ManyToManyField(
        Product,
        through='Order_Product',
        through_fields=('order', 'product')
    )
    customer_markup     = models.PositiveSmallIntegerField(help_text='Ricarico', null=False, blank=False)
    customer_discount   = models.PositiveSmallIntegerField(help_text='Sconto', null=False, blank=False)
    timestamp           = models.DateTimeField(help_text='Data e Ora', auto_now=True, null=False, blank=False)
    
    def get_subtotal_adjusted(self):
        subtotal = 0.0
        relations = Order_Product.objects.filter(order=self)
        for relation in relations:
            subtotal += relation.product_price_adjusted * relation.product_quantity
        return f'{subtotal:.2f}'

    def get_subtotal(self):
        subtotal = 0.0
        relations = Order_Product.objects.filter(order=self)
        for relation in relations:
            subtotal += relation.product_price * relation.product_quantity
        return f'{subtotal:.2f}'
    
    # status              =
    # subtotal            = models.FloatField(help_text='Subtotale', null=False, blank=False)
    # total               = models.FloatField(help_text='Totale', null=False, blank=False)


class Order_Product(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product  = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_quantity = models.PositiveSmallIntegerField(help_text='Quantita\'', null=False, blank=False)
    product_price = models.FloatField(help_text='', null=False, blank=False)
    product_price_adjusted = models.FloatField(help_text='Prezzo', null=False, blank=False)