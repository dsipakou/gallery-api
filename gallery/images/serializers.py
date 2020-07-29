from rest_framework import serializers

from images.models import Image, Like
from datetime import datetime


class ImageSerializer(serializers.ModelSerializer):
    photo_preview = serializers.ImageField(read_only=True)

    class Meta:
        model = Image
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class ImageByDateSerializer(serializers.Serializer):
    date = serializers.CharField()

    def validate_date(self, value):
        validated_date = datetime.strptime(value, "%Y-%m")
        return validated_date
