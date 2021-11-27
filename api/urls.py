from django.urls import path, include
from rest_framework import routers
from projects import views



urlpatterns = [
    path('projects/', include('projects.urls')),
]