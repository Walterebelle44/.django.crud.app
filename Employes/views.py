from django.shortcuts import render

from Employes.models import Employe

# Create your views here.

def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, 'employes/liste_employes.html', {'employes': employes})