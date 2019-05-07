from django.db import models
from django.urls import reverse


class Product(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=25)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.FileField(default='default.jpg', upload_to='images_pics', null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.titre)

    class Meta:
        unique_together = ('titre', 'slug')

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse('single-product', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='images_pics', null=True, blank=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product.titre
