from django.urls import path
from . import views

urlpatterns = [

    path('profile/', views.profile, name='blog-profile'),
    path('register/', views.register, name='blog-register'),

]
