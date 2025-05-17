from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("listar/", views.listar_itens, name="listar_itens"),
    path("adicionar/", views.adicionar_item, name="adicionar_item")
]
