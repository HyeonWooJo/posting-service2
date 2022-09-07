import os

from rest_framework            import status
from rest_framework.generics   import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.views      import APIView
from rest_framework.response   import Response

from .models      import Posting
from .serializers import PostingSerializer
from .utils       import check_psword


# 게시글 리스트 조회
class PostingListAPIView(APIView):
    def get(self, request):
        """
        게시글 리스트 조회 API
        :return: 게시글 리스트
        """
        posts      = Posting.objects.all()
        serializer = PostingSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 게시글 생성, 수정, 삭제 
class PostingDetailAPIView(APIView):
    def post(self, request):
        """
        게시글 생성 API
        :param: title: str
        :param: content: str
        :param: psword: str
        :return: 게시글 생성 성공 여부
        """
        serializer = PostingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


    def patch(self, request, id):
        """
        게시글 수정 API
        :param: id: int
        :return: 게시글 삭제 성공 여부
        """
        posting    = Posting.objects.get(id=id)
        serializer = PostingSerializer(posting, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)


    def delete(self, request, id):
        """
        게시글 삭제 API
        :param: id: int
        :return: 게시글 삭제 성공 여부
        """
        posting  = Posting.objects.get(id=id)
        input_pw = request.data['psword']

        if not check_psword(input_pw, posting):
            raise ValidationError("비밀번호가 맞지 않습니다.")

        posting.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)