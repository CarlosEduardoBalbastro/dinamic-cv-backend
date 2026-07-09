from django.urls import path
from .views import CertificacionListCreateView

urlpatterns = [
    path('', CertificacionListCreateView.as_view(), name='certificacion-list-create'),
]