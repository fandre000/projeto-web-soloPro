
from django.contrib import admin
from django.urls import path, include
from app_soloPro import views




urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'), 
    path('login/', views.login, name='login'),
    path('detalhes/', views.detalhes, name='detalhes'),
    path('candidatos/', views.candidatos, name='candidatos'),
    path('vagas/', views.vagas, name='vagas'),
    path('teste/', views.teste, name='teste'),
    path('salvar/', views.salvar, name='salvar'),
    path('editar_candidato/<int:id>', views.editar_candidato, name='editar_candidato'),
    path('editar_vaga/<int:id>', views.editar_vaga, name='editar_vaga'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete_vaga/<int:id>', views.delete_vaga, name='delete_vaga'),
    path('delete_candidato/<int:id>', views.delete_candidato, name='delete_candidato'),
    path('update_candidato/<int:id>', views.update_candidato, name='update_candidato'),
    path('update_vaga/<int:id>', views.update_vaga, name='update_vaga'),

    path('exemplo/', views.exemplo, name='exemplo'),
    path('adicionar_candidatos/', views.adicionar_candidatos, name='adicionar_candidatos'),
    path('adicionar_vagas/', views.adicionar_vagas, name='adicionar_vagas'),

    

    path('salvar_candidato/', views.salvar_candidato, name='salvar_candidato'),

    path('salvar_vagas/', views.salvar_vagas, name='salvar_vagas'),

    path('ver_detalhes/<int:id>', views.ver_detalhes, name='ver_detalhes'),
    path('ver_detalhes_vaga/<int:id>', views.ver_detalhes_vaga, name='ver_detalhes_vaga'),

    

    

    


]





