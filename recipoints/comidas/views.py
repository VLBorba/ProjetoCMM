from django.shortcuts import render
from .models import home, bares, comidas, cinemas, lazer, praias, turismo
from django.urls import reverse_lazy

def homepagina(request):
    inicio = home.objects.all()
    return render(request, "comidasestrutura/home.html", {"inicio": inicio})
    sucecess_url = reverse_lazy(home_rota)

def bareslista(request):
    place = bares.objects.all()
    return render(request, "comidasestrutura/bareslista.html", {"place": place})
    sucecess_url = reverse_lazy(bares_rota)

def comidaslista(request):
    place = comidas.objects.all()
    return render(request, "comidasestrutura/comidaslista.html", {"place": place})
    sucecess_url = reverse_lazy(comidas_rota)

def cinemalista(request):
    place = cinemas.objects.all()
    return render(request, "comidasestrutura/cinemalista.html", {"place": place})
    sucecess_url = reverse_lazy(cinema_rota)

def lazerlista(request):
    place = lazer.objects.all()
    return render(request, "comidasestrutura/lazerlista.html", {"place": place})
    sucecess_url = reverse_lazy(lazer_rota)

def praiaslista(request):
    place = praias.objects.all()
    return render(request, "comidasestrutura/praiaslista.html", {"place": place})
    sucecess_url = reverse_lazy(praias_rota)

def turismolista(request):
    place = turismo.objects.all()
    return render(request, "comidasestrutura/turismolista.html", {"place": place})
    sucecess_url = reverse_lazy(turismo_rota)
