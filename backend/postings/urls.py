
from django.urls import path

from .views import (
    PostingListCreateAPIView,
    PostingDeleteUpdateAPIView
)

urlpatterns = [
    path("", PostingListCreateAPIView.as_view()),
    path("<int:id>", PostingDeleteUpdateAPIView.as_view())
]