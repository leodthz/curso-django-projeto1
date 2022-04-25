from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('HOME teste')


def contato(request):
    return HttpResponse('CONTATO a')


def sobre(request):
    return HttpResponse('SOBRE a')
