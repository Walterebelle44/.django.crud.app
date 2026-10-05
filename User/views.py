from multiprocessing.connection import Client

from django.shortcuts import render

from .models import User

# Create your views here.

def liste_users(request):
    users = User.objects.all()
    return render(request, 'users/liste_users.html', {'users': users})


def liste_clients(request):
    clients = User.objects.all()
    return render(request, 'users/liste_clients.html', {'clients': clients})


def afficher_user(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/afficher_user.html', {'user': user})

def afficher_client(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'users/afficher_client.html', {'client': client})


def ajouter_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        prenom = request.POST['prenom']
        email = request.POST['email']
        password = request.POST['password']
        user = User(name=name, prenom=prenom, email=email, password=password)
        user.save()
        return render(request, 'users/ajouter_user.html', {'message': 'User ajouté avec succès !'})
    return render(request, 'users/ajouter_user.html')

def ajouter_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        prenom = request.POST['prenom']
        email = request.POST['email']
        password = request.POST['password']
        client = Client(name=name, prenom=prenom, email=email, password=password)
        client.save()
        return render(request, 'users/ajouter_client.html', {'message': 'Client ajouté avec succès !'})
    return render(request, 'users/ajouter_client.html')


def supprimer_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return render(request, 'users/supprimer_user.html', {'message': 'User supprimé avec succès !'})

def supprimer_client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return render(request, 'users/supprimer_client.html', {'message': 'Client supprimé avec succès !'})


def modifier_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.prenom = request.POST['prenom']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        return render(request, 'users/modifier_user.html', {'user': user, 'message': 'User modifié avec succès !'})
    return render(request, 'users/modifier_user.html', {'user': user})


def modifier_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.name = request.POST['name']
        client.prenom = request.POST['prenom']
        client.email = request.POST['email']
        client.password = request.POST['password']
        client.save()
        return render(request, 'users/modifier_client.html', {'client': client, 'message': 'Client modifié avec succès !'})
    return render(request, 'users/modifier_client.html', {'client': client})


def rechercher_user(request):
    if request.method == 'POST':
        query = request.POST['query']
        users = User.objects.filter(name__icontains=query)
        return render(request, 'users/rechercher_user.html', {'users': users, 'query': query})
    return render(request, 'users/rechercher_user.html')

def rechercher_client(request):
    if request.method == 'POST':
        query = request.POST['query']
        clients = Client.objects.filter(name__icontains=query)
        return render(request, 'users/rechercher_client.html', {'clients': clients, 'query': query})
    return render(request, 'users/rechercher_client.html')


def voir_toutes_personnes_systeme(request):
    users = User.objects.all()
    clients = Client.objects.all()
    return render(request, 'users/voir_toutes_personnes_systeme.html', {'users': users, 'clients': clients})

