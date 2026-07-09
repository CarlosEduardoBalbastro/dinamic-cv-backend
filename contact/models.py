from django.db import models

class RedSocial(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.URLField(max_length=255) 

    def __str__(self):
        return self.nombre
