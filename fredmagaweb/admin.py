from django.contrib import admin
from .models import PortfolioItem, Curriculo, Certificate

def make_unpublished(modeladmin, request, queryset):
    queryset.update(publicado=False)
make_unpublished.short_description = "Despublicar casos selecionados"

def make_published(modeladmin, request, queryset):
    queryset.update(publicado=True)
make_published.short_description = "Publicar casos selecionados"

class PortfolioItemAdmin(admin.ModelAdmin):
    actions = [make_published, make_unpublished]
    list_display = ('title', 'publicado')

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(Curriculo)
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title',)