
from django.contrib import admin
from django.urls import path
from app_soloPro import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login, name='login'),
    path('teste/', views.teste, name='teste'),
    path('candidatos/', views.candidatos, name='candidatos'),
    path('vagas/', views.vagas, name='vagas'),


]





