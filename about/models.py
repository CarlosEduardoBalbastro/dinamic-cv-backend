from django.db import models

class Certificacion(models.Model):
    titulo = models.CharField(max_length=150)
    institucion = models.CharField(max_length=150)
    anio = models.IntegerField() 
    imagen = models.CharField(max_length=255) 

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"
