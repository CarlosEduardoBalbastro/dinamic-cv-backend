
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/proyectos/', include('projects.urls')),
    path('api/certificaciones/', include('about.urls')),
    path('api/contacto/', include('contact.urls'))
]
