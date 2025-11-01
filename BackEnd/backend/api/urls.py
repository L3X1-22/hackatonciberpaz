# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .viewsets import SeccionViewSet, ConceptoViewSet, CitaBibliograficaViewSet

# Crear router para ViewSets
router = DefaultRouter()
router.register(r'secciones', SeccionViewSet, basename='seccion')
router.register(r'conceptos', ConceptoViewSet, basename='concepto')
router.register(r'citas', CitaBibliograficaViewSet, basename='cita')

urlpatterns = [
    # Overview
    path('', views.api_overview, name='api-overview'),
    
    # Router URLs (incluye browsable API)
    path('', include(router.urls)),
    
    # URLs específicas adicionales
    path('secciones/resumen/', views.SeccionResumenListView.as_view(), name='seccion-resumen'),
    path('secciones/<int:seccion_id>/conceptos/', views.ConceptosPorSeccionView.as_view(), name='conceptos-por-seccion'),
    path('buscar/', views.BuscarConceptosView.as_view(), name='buscar-conceptos'),
]