from rest_framework import serializers

from .models import Posting


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = [
            'title',
            'context',
            'psword',
            'created_at',
            'modified_at'
        ]
        extra_kwargs = {
            "psword": {"write_only": True},
        }
        
    def create(self, validated_data):
        post = Posting(**validated_data)

        post.save()
        return post