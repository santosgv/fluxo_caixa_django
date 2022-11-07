from . import views
from django.urls import path

urlpatterns = [
    path('adicionar', views.adicionar, name='adicionar'),
    path('visualizar', views.visualizar, name='visualizar'),
]
