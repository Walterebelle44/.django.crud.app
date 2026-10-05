from django.contrib import admin

from .models import User
from .models import Client

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'prenom', 'email', 'password')
    search_fields = ('name', 'prenom', 'email')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'prenom', 'email', 'password')
    search_fields = ('name', 'prenom', 'email')