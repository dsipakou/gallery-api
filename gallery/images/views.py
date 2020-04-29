from rest_framework.generics import ListAPIView

from images.models import Image
from images.serializers import ImageSerializer


class ImageListView(ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all().order_by("-date_created")
