from django.urls import path
from . import views

urlpatterns = [
    path('definir_planejamento/', views.definir_planejamento, name="definir_planejamento"),
    path('update_valor_categoria/<int:id>/', views.update_valor_categoria, name="update_valor_categoria"),
    path('ver_planejamento/', views.ver_planejamento, name="ver_planejamento"),
    path('metas/', views.metas, name="metas"),
    path('criar_meta/', views.criar_meta, name="criar_meta"),
    path('deletar_meta/<int:id>', views.deletar_meta, name="deletar_meta"),
]