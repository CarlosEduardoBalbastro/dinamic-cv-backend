from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=150)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField()
    tecnologias = models.JSONField(default=list)
    link= models.URLField(max_length=200, blank=True, null=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
