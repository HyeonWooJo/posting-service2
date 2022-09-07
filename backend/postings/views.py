import os
import bcrypt

from rest_framework import status
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models      import Posting
from .serializers import PostingSerializer


# 게시글 생성 및 리스트 조회
class PostsAPI(APIView):
    def get(self, request):
        """
        게시글 리스트 조회 API
        :return: 게시글 리스트
        """
        posts = Posting.objects.all()
        serializer = PostingSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        게시글 생성 API
        :param: title: str
        :param: content: str
        :param: password: str
        :return: 게시글 생성 성공 여부
        """
        serializer = PostingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_OK)