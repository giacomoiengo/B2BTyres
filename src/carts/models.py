from django.db import models
from accounts.models import Customer
from products.models import Product



class Cart(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(
        Product,
        through='Cart_Product',
        through_fields=('cart', 'product'),
    )

    def get_subtotal(self):
        subtotal = 0.0
        relations = Cart_Product.objects.filter(cart=self)
        for relation in relations:
            subtotal += relation.product.adjust_price(self.customer) * relation.quantity
        return f'{subtotal:.2f}'

    def get_total(self):
        pass


class Cart_Product(models.Model):
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False, default=1)



