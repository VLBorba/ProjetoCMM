from django.shortcuts import render
from .models import home, bares, comidas, cinemas, lazer, praias, turismo
from django.urls import reverse_lazy

def homepagina(request):
    inicio = home.objects.all()
    return render(request, "estrutura/home.html", {"inicio": inicio})
    sucecess_url = reverse_lazy(home_rota)

def bareslista(request):
    place = bares.objects.all()
    return render(request, "estrutura/bareslista.html", {"place": place})
    sucecess_url = reverse_lazy(bares_rota)

def comidaslista(request):
    place = comidas.objects.all()
    return render(request, "estrutura/comidaslista.html", {"place": place})
    sucecess_url = reverse_lazy(comidas_rota)

def cinemalista(request):
    cine = cinemas.objects.all()
    return render(request, "estrutura/cinemalista.html", {"cine": cine})
    sucecess_url = reverse_lazy(cinema_rota)

def lazerlista(request):
    place = lazer.objects.all()
    return render(request, "estrutura/lazerlista.html", {"place": place})
    sucecess_url = reverse_lazy(lazer_rota)

def praiaslista(request):
    place = praias.objects.all()
    return render(request, "estrutura/praiaslista.html", {"place": place})
    sucecess_url = reverse_lazy(praias_rota)

def turismolista(request):
    place = turismo.objects.all()
    return render(request, "estrutura/turismolista.html", {"place": place})
    sucecess_url = reverse_lazy(turismo_rota)
