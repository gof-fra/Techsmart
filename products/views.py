from django.shortcuts import render, Http404
from .models import Product, ProductImage


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/productHome.html', context)


def search(request):
    try:
        search = request.GET.get('search')
    except:
        search = None
    if search:
        products = Product.objects.filter(titre__icontains=search)
        context = {'query': search, 'products': products}
        templates = 'products/result.html'
    else:
        products = Product.objects.all()
        context = {'products': products}
        templates = 'products/productHome.html'
    return render(request, templates, context)


def all(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/allProducts.html', context)


def single(request, slug=None):
    try:
        product = Product.objects.get(slug=slug)
        images = ProductImage.objects.filter(product=product)
        context = {'product': product, 'images': images}
        return render(request, 'products/single.html', context)
    except:
        raise Http404
