from django.contrib import admin
from .models import Documento


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "fecha_publicacion")
    search_fields = ("titulo", "descripcion")
    list_filter = ("tipo",)
