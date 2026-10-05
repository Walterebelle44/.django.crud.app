from django.contrib import admin

# Register your models here.

from .models import Livres

@admin.register(Livres)
class LivresAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'description')
    search_fields = ('name', 'author', 'description')