from rest_framework import viewsets
from .models import ContentBlock, Bibliography
from .serializers import ContentBlockSerializer, BibliographySerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

class SoloLecturaParaAnonimos(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

class ContentBlockViewSet(viewsets.ModelViewSet):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer
    permission_classes = [SoloLecturaParaAnonimos]

class BibliographyViewSet(viewsets.ModelViewSet):
    queryset = Bibliography.objects.all()
    serializer_class = BibliographySerializer
    permission_classes = [SoloLecturaParaAnonimos]
