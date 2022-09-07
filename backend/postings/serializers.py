import bcrypt
import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Posting


def hash_psword(psword: str):
    """
    bcrypt를 이용한 비밀번호 암호화
    :param password: string
    :return: 암호호된 비밀번호
    """
    hashed_psword = bcrypt.hashpw(
        psword.encode('utf-8'),
        bcrypt.gensalt()
    )
    decode_psword = hashed_psword.decode('utf-8')
    return decode_psword


class PostingSerializer(serializers.ModelSerializer):
    """
    Posting Serialization
    """
    class Meta:
        model = Posting
        # fields = "__all__"
        exclude = ["id"]
        extra_kwargs = {
            "psword": {"write_only": True},
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

    def validate_title(self, title: str):
        """
        제목 유효성 검사
            - 최대 20자 제하
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
        instance.psword = hash_psword(validated_data.pop('psword'))
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.password = hash_psword(validated_data.get('password', instance.password))
        instance.save()

        return super().update(instance, validated_data)