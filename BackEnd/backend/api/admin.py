# api/admin.py

from django.contrib import admin
from .models import Seccion, Concepto, Referencia, CitaBibliografica

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden', 'total_conceptos']
    list_editable = ['orden']
    search_fields = ['nombre', 'descripcion']
    
    def total_conceptos(self, obj):
        return obj.conceptos.count()
    total_conceptos.short_description = 'Total Conceptos'

@admin.register(Concepto)
class ConceptoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'subtema', 'seccion', 'orden']
    list_filter = ['seccion']
    search_fields = ['subtema', 'descripcion']
    list_editable = ['orden']

@admin.register(Referencia)
class ReferenciaAdmin(admin.ModelAdmin):
    list_display = ['concepto', 'tipo', 'autores', 'año']
    list_filter = ['tipo', 'año']
    search_fields = ['cita', 'autores']

@admin.register(CitaBibliografica)
class CitaBibliograficaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'cita_completa_short', 'año_publicacion']
    search_fields = ['cita_completa', 'autores']
    
    def cita_completa_short(self, obj):
        return obj.cita_completa[:100] + '...' if len(obj.cita_completa) > 100 else obj.cita_completa
    cita_completa_short.short_description = 'Cita'