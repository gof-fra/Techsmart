from django.contrib import admin

from .models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['titre']
    list_display = ['__unicode__', 'titre', 'price', 'date', 'image', 'active']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['date']
    prepopulated_fields = {"slug": ("titre",)}

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)
