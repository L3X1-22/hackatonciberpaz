# api/models.py

from django.db import models

class Seccion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"
        ordering = ['orden']
    
    def __str__(self):
        return self.nombre

class Concepto(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='conceptos')
    numero = models.PositiveIntegerField()
    subtema = models.CharField(max_length=300)
    descripcion = models.TextField()
    orden = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Concepto"
        verbose_name_plural = "Conceptos"
        ordering = ['seccion', 'orden']
        unique_together = ['seccion', 'numero']
    
    def __str__(self):
        return f"{self.numero}. {self.subtema}"

class Referencia(models.Model):
    TIPO_REFERENCIA = [
        ('libro', 'Libro'),
        ('articulo', 'Artículo'),
        ('sitio_web', 'Sitio Web'),
        ('video', 'Video'),
        ('otro', 'Otro'),
    ]
    
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE, related_name='referencias')
    cita = models.TextField(help_text="Formato completo de la cita bibliográfica")
    enlace = models.URLField(max_length=500, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_REFERENCIA, default='articulo')
    autores = models.CharField(max_length=300, blank=True)
    año = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"
    
    def __str__(self):
        return f"Ref: {self.concepto.subtema[:50]}..."

class CitaBibliografica(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    cita_completa = models.TextField(help_text="Cita bibliográfica completa")
    enlace = models.URLField(max_length=500, blank=True)
    tipo_recurso = models.CharField(max_length=100, blank=True)
    autores = models.CharField(max_length=300, blank=True)
    año_publicacion = models.PositiveIntegerField(null=True, blank=True)
    revista_editorial = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = "Cita Bibliográfica"
        verbose_name_plural = "Citas Bibliográficas"
        ordering = ['numero']
    
    def __str__(self):
        return f"[{self.numero}] {self.cita_completa[:100]}..."