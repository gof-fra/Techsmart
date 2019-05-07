from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
admin.autodiscover()


urlpatterns = [

    path('product/', views.product, name='products'),
    path('s/', views.search, name='search'),
    path('products/', views.all, name='all-products'),
    path('product/<str:slug>/', views.single, name='single-product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
