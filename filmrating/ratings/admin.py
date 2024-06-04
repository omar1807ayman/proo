# ratings/admin.py
from django.contrib import admin
from .models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    fields = ('title', 'description', 'release_date', 'image')
