from django.db import models

from products.models import Product


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=True)
    product = models.ForeignKey(Product, on_delete=True)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.titre


class Cart(models.Model):
    # items = models.ManyToManyField(CartItem, null=True, blank=True)
    # products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)


def __unicode__(self):
    return "Cart id: %s" %(self.id)
