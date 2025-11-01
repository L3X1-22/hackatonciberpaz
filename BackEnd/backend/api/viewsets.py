# api/viewsets.py

from rest_framework import viewsets, mixins
from .models import Seccion, Concepto, Referencia, CitaBibliografica
from .serializers import *

class SeccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Seccion.objects.prefetch_related('conceptos').all()
    serializer_class = SeccionSerializer

class ConceptoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Concepto.objects.select_related('seccion').prefetch_related('referencias').all()
    serializer_class = ConceptoSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ConceptoDetalladoSerializer
        return ConceptoSerializer

class CitaBibliograficaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CitaBibliografica.objects.all()
    serializer_class = CitaBibliograficaSerializer

# Si quieres permitir crear/editar desde la API:
class SeccionManagementViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

class ConceptoManagementViewSet(viewsets.ModelViewSet):
    queryset = Concepto.objects.all()
    serializer_class = ConceptoSerializer