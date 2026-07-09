from rest_framework import serializers
from .models import Certificacion


class CertificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificacion
        fields = ['id', 'titulo', 'institucion', 'anio', 'imagen']  
        