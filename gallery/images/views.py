from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from images.models import Image
from images.serializers import ImageSerializer


class ImageListView(ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all().order_by("date_created").reverse()[:5]


class ImageView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = "uuid"

    def retrieve(self, request, *args, **kwargs):
        image = self.get_object()
        return Response(self.get_serializer(image).data)
