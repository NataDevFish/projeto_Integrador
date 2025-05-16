from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def listar_itens(request):
    return render(request, "listar_itens.html")


def adicionar_item(request):
    return render(request, "adicionar_item.html")
