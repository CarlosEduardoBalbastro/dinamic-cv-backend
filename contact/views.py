from rest_framework import generics
from .models import RedSocial
from .serializers import RedSocialSerializer

class RedSocialListCreateView(generics.ListCreateAPIView):
    queryset = RedSocial.objects.all()
    serializer_class = RedSocialSerializer
