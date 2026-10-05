from urllib import request
from django.shortcuts import render

from User import models

# Create your views here.

def liste_livres(request):
    livres = models.Livres.objects.all()
    return render(request, 'livres/liste_livres.html', {'livres': livres})

def liste_cahiers(request):
    cahiers = models.Cahiers.objects.all()
    return render(request, 'livres/liste_cahiers.html', {'cahiers': cahiers})

