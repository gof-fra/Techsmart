from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from products.models import Product
from .models import Cart, CartItem


def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {'cart': cart}
    else:
        message_empty = "Please keep shopping, Your Cart is empty"
        context = {'empty': True, 'message_empty': message_empty}
    template = 'carts/view.html'
    return render(request, template, context)


def update_cart(request, slug):
    request.session.set_expiry(300)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        print("that ok")

    # if not cart_item in cart.item.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)

    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse('carts'))
