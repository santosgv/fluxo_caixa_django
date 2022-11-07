from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

def visualizar(request):
    return HttpResponse('visualizar')

def adicionar(request):
    return HttpResponse('adicionar')