from rest_framework import serializers

from images.models import Image, Like


class ImageSerializer(serializers.ModelSerializer):
    photo_preview = serializers.ImageField(read_only=True)

    class Meta:
        model = Image
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
