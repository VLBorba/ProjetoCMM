
from django.contrib import admin
from django.urls import path
from comidas.views import homepagina, bareslista, comidaslista, cinemalista, lazerlista, praiaslista, turismolista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepagina, name="home_rota"),
    path('bares', bareslista,name="bares_rota"),
    path('comidas', comidaslista,name="comidas_rota"),
    path('cinemas', cinemalista,name="cinemas_rota"),
    path('lazer', lazerlista,name="lazer_rota"),
    path('praias', praiaslista,name="praias_rota"),
    path('turismo', turismolista,name="turismo_rota"),
]
