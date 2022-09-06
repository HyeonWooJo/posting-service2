from django.urls import path

from .views import HelloAPI

urlpatterns = [
    path('', HelloAPI)
]