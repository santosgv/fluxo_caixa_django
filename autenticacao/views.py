from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User


def home(request):
    return HttpResponse('home')


def logar(request):
    return HttpResponse('foi')


def cadastrar(request):
    return HttpResponse('cadastrar')