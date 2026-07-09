from rest_framework import generics
from .models import Certificacion
from .serializers import CertificacionSerializer

class CertificacionListCreateView(generics.ListCreateAPIView):
    queryset = Certificacion.objects.all()
    serializer_class = CertificacionSerializer