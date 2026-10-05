from django.urls import path
from . import views


urlpatterns = [
    path('', views.liste_users, name='liste_users'),
    path('users/', views.liste_users, name='liste_users'),
    path('clients/', views.liste_clients, name='liste_clients'),
    path('users/<int:user_id>/', views.afficher_user, name='afficher_user'),
    path('clients/<int:client_id>/', views.afficher_client, name='afficher_client'),
    path('users/ajouter/', views.ajouter_user, name='ajouter_user'),
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),
    path('users/supprimer/<int:user_id>/', views.supprimer_user, name='supprimer_user'),
    path('clients/supprimer/<int:client_id>/', views.supprimer_client,name='supprimer_client'),
    path('users/ajouter/', views.ajouter_user, name='ajouter_user'),
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),
]