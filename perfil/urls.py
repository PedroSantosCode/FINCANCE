from django.urls import path 
from . import views
from . import api_views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('gerenciar/', views.gerenciar, name="gerenciar"),
    path('cadastrar_banco/', views.cadastrar_banco, name="cadastrar_banco"),
    path('deletar_banco/<int:id>/', views.deletar_banco, name='deletar_banco'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name="cadastrar_categoria"),
    path('update_categoria/<int:id>/', views.update_categoria, name="update_categoria"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('calculadora/', views.calculadora, name="calculadora"),
    path('api/sugerir_categoria/', api_views.sugerir_categoria_view, name="sugerir_categoria"),
    path('api/resumo/', views.api_resumo, name="api_resumo"),
]