from django.urls import path
from . import views


urlpatterns = [

    path('carts/', views.view, name='cart'),
    path('carts/<str:slug>/', views.update_cart, name='update-cart'),
]
