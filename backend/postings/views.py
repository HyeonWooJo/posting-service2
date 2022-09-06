import os
import bcrypt

from rest_framework import status
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models      import Posting
from .serializers import PostingSerializer


class PostsAPI(APIView):
    def get(self, request):
        posts = Posting.objects.all()
        posts_serializer = PostingSerializer(posts, many=True)
        return Response(posts_serializer.data, status=status.HTTP_200_OK)