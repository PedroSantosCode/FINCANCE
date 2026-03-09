from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('criar/', views.blog_create, name='blog_create'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('<slug:slug>/editar/', views.blog_edit, name='blog_edit'),
]
