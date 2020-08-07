from django.urls import path, include
from .views import homepage, about, error_404_view

urlpatterns = [
    path("", homepage, name="homepage"),
    path('about/', about, name="about"),
    
]

handler404 = 'home.views.error_404_view'