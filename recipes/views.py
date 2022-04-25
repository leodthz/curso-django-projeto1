from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse(render(request, 'recipes/home.html'))


def contato(request):
    return HttpResponse('CONTATO a')


def sobre(request):
    return HttpResponse('SOBRE a')
