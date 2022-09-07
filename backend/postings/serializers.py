import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models        import Posting
from postings.utils import hash_psword, check_psword


class PostingSerializer(serializers.ModelSerializer):
    """
    Posting Serialization
    """
    class Meta:
        model = Posting
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }

    def validate_psword(self, psword:str):
        """
        비밀번호 유효성 검사
            - 6자 이상
            - 숫자 1개 포함
        :param password: string
        :return: 암호화된 비밀번호
        """
        REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$'

        if not re.match(REGEX_PASSWORD, psword):
            raise ValidationError('INVALID_PASSWORD')

        return psword

    def validate_title(self, title: str):
        """
        제목 유효성 검사
            - 최대 20자 제한
        :param title: string
        :return: title
        """
        if len(title) > 20:
            raise ValidationError("제목은 최대 20자 까지만 쓸 수 있습니다.")
        return title

    def validate_content(self, content: str):
        """
        본문 유효성 검사
            - 최대 200자 제한
        :param content: string
        :return: content
        """
        if len(content) > 200:
            raise ValidationError("본문은 최대 200자 까지만 쓸 수 있습니다.")
        return content

    def create(self, validated_data):
        """
        일반 비밀번호에서 암호화된 비밀번호로 변경하여 게시물 저장
        :param validated_data:
        :return: Created posting object
        """
        psword = validated_data.pop("psword", None)
        instance = self.Meta.model(**validated_data)

        if psword is not None:
            instance.psword = hash_psword(psword)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        """
        암호화된 비밀번호로 게시글 인스턴스 수정
        :param instance:
        :param validated_data:
        :return: instance
        """
        psword = validated_data['psword']
        if not check_psword(psword, instance):
            raise ValidationError("비밀번호가 맞지 않습니다.")
        
        instance.title = validated_data['title']
        instance.context = validated_data['context']
        instance.save()
        return instance