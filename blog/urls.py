from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )

from . import views

urlpatterns = [

    path('', views.home, name='smartech-home'),
    path('home/', views.home, name='smartech-home'),
    path('admin/', views.admin, name='admin'),
    path('industry/', views.industry, name='industry'),
    path('mobile/', views.mobile, name='mobile'),
    path('formation/', views.forma, name='formation'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('blog/post/', PostListView.as_view(), name='smartech-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
