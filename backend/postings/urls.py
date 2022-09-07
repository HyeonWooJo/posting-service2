
from django.urls import path

from .views import PostsAPI

urlpatterns = [
    path("postings", PostsAPI.as_view())
]