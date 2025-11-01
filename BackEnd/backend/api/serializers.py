# api/serializers.py

from rest_framework import serializers
from .models import Seccion, Concepto, Referencia, CitaBibliografica

class CitaBibliograficaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaBibliografica
        fields = '__all__'

class ReferenciaSerializer(serializers.ModelSerializer):
    cita_detalle = serializers.CharField(source='cita', read_only=True)
    enlace_url = serializers.CharField(source='enlace', read_only=True)
    
    class Meta:
        model = Referencia
        fields = ['id', 'cita', 'cita_detalle', 'enlace', 'enlace_url', 'tipo', 'autores', 'año']

class ConceptoSerializer(serializers.ModelSerializer):
    referencias = ReferenciaSerializer(many=True, read_only=True)
    seccion_nombre = serializers.CharField(source='seccion.nombre', read_only=True)
    
    class Meta:
        model = Concepto
        fields = ['id', 'numero', 'seccion', 'seccion_nombre', 'subtema', 'descripcion', 'orden', 'referencias']

class SeccionSerializer(serializers.ModelSerializer):
    conceptos = ConceptoSerializer(many=True, read_only=True)
    total_conceptos = serializers.SerializerMethodField()
    
    class Meta:
        model = Seccion
        fields = ['id', 'nombre', 'descripcion', 'orden', 'conceptos', 'total_conceptos']
    
    def get_total_conceptos(self, obj):
        return obj.conceptos.count()

class SeccionResumenSerializer(serializers.ModelSerializer):
    total_conceptos = serializers.SerializerMethodField()
    
    class Meta:
        model = Seccion
        fields = ['id', 'nombre', 'descripcion', 'orden', 'total_conceptos']
    
    def get_total_conceptos(self, obj):
        return obj.conceptos.count()

class ConceptoDetalladoSerializer(serializers.ModelSerializer):
    seccion_info = SeccionResumenSerializer(source='seccion', read_only=True)
    referencias = ReferenciaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Concepto
        fields = ['id', 'numero', 'subtema', 'descripcion', 'orden', 'seccion_info', 'referencias']