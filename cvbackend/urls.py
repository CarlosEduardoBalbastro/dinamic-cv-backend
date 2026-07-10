from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', obtain_auth_token, name='api_login'),
    path('api/proyectos/', include('projects.urls')),
    path('api/certificaciones/', include('about.urls')),
    path('api/contacto/', include('contact.urls')),
]
