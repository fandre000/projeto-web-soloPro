from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

def detalhes(request):
    return render(request, 'home/detalhes.html')

def candidatos(request):
    return render(request, 'home/candidatos.html')
def vagas(request):
    return render(request, 'home/vagas.html')
