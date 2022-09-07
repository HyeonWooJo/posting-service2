from rest_framework import serializers

from .models import Posting


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        # fields = "__all__"
        exclude = ["id"]
        extra_kwargs = {
            "psword": {"write_only": True},
        }