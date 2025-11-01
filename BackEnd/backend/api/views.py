# api/views.py

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Prefetch
from .models import Seccion, Concepto, Referencia, CitaBibliografica
from .serializers import (
    SeccionSerializer, ConceptoSerializer, ConceptoDetalladoSerializer,
    CitaBibliograficaSerializer, SeccionResumenSerializer
)

@api_view(['GET'])
def api_overview(request):
    endpoints = {
        'secciones': '/api/secciones/',
        'secciones_resumen': '/api/secciones/resumen/',
        'conceptos': '/api/conceptos/',
        'conceptos_por_seccion': '/api/secciones/{id}/conceptos/',
        'concepto_detalle': '/api/conceptos/{id}/',
        'citas_bibliograficas': '/api/citas/',
        'buscar': '/api/buscar/?q=termino',
    }
    return Response(endpoints)

class SeccionListView(generics.ListAPIView):
    queryset = Seccion.objects.prefetch_related('conceptos').all()
    serializer_class = SeccionSerializer

class SeccionResumenListView(generics.ListAPIView):
    queryset = Seccion.objects.all()
    serializer_class = SeccionResumenSerializer

class SeccionDetailView(generics.RetrieveAPIView):
    queryset = Seccion.objects.prefetch_related(
        Prefetch('conceptos', queryset=Concepto.objects.prefetch_related('referencias'))
    )
    serializer_class = SeccionSerializer

class ConceptoListView(generics.ListAPIView):
    queryset = Concepto.objects.select_related('seccion').prefetch_related('referencias').all()
    serializer_class = ConceptoSerializer

class ConceptoDetailView(generics.RetrieveAPIView):
    queryset = Concepto.objects.select_related('seccion').prefetch_related('referencias')
    serializer_class = ConceptoDetalladoSerializer

class ConceptosPorSeccionView(generics.ListAPIView):
    serializer_class = ConceptoSerializer
    
    def get_queryset(self):
        seccion_id = self.kwargs['seccion_id']
        return Concepto.objects.filter(seccion_id=seccion_id).prefetch_related('referencias')

class CitaBibliograficaListView(generics.ListAPIView):
    queryset = CitaBibliografica.objects.all()
    serializer_class = CitaBibliograficaSerializer

class BuscarConceptosView(generics.ListAPIView):
    serializer_class = ConceptoSerializer
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Concepto.objects.filter(
                models.Q(subtema__icontains=query) |
                models.Q(descripcion__icontains=query) |
                models.Q(seccion__nombre__icontains=query)
            ).select_related('seccion').prefetch_related('referencias')
        return Concepto.objects.none()