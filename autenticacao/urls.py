from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('logar/', views.logar, name='logar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
