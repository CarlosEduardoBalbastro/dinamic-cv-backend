from rest_framework import serializers
from .models import RedSocial

class RedSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedSocial
        fields = ['id', 'nombre', 'url']