import bcrypt
from rest_framework.pagination import PageNumberPagination
from postings.models import Posting


def hash_psword(psword: str):
    """
    bcrypt를 이용한 비밀번호 암호화
    :param psword: string
    :return: 암호호된 비밀번호
    """
    hashed_psword = bcrypt.hashpw(psword.encode("utf-8"), bcrypt.gensalt())
    decode_psword = hashed_psword.decode("utf-8")
    return decode_psword


def check_psword(psword: str, instance: Posting):
    """
    비밀번호 체크
    :param psword: string
    :param instance: PostingSerializer
    :return: Boolean
    """
    encoded_psword = psword.encode("utf-8")
    encoded_db_psword = instance.psword.encode("utf-8")
    return bcrypt.checkpw(encoded_psword, encoded_db_psword)


class PostPageNumberPagination(PageNumberPagination):
    page_size = 20