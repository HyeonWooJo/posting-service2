
from django.urls import path

from .views import (
    PostingListAPIView,
    PostingDetailAPIView
)

urlpatterns = [
    path("", PostingListAPIView.as_view()),
    path("/detail", PostingDetailAPIView.as_view()),
    path("/detail/<int:id>", PostingDetailAPIView.as_view())
]