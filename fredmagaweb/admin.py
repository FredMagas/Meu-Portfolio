from django.contrib import admin
from .models import PortfolioItem

admin.site.register(PortfolioItem)

def make_unpublished(modeladmin, request, queryset):
    queryset.update(publicado=False)
make_unpublished.short_description = "Despublicar casos selecionados"

def make_published(modeladmin, request, queryset):
    queryset.update(publicado=True)
make_published.short_description = "Publicar casos selecionados"