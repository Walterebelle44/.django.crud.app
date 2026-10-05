from django.contrib import admin

from Employes.models import Employe

# Register your models here.

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prenom', 'email', 'password')
    search_fields = ('name', 'prenom', 'email')