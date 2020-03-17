from rest_framework import serializers

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    thumbnail_image = serializers.ReadOnlyField(source='photo_preview.url')

    class Meta:
        model = Image
        fields = '__all__'
