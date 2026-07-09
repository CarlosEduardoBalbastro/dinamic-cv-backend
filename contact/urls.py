from django.urls import path
from .views import RedSocialListCreateView

urlpatterns = [
    path('', RedSocialListCreateView.as_view(), name='redsocial-list-create'),
]