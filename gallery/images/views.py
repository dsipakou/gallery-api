from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response

from images.models import Image, Like
from images.serializers import ImageSerializer, LikeSerializer


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


class LikeView(GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_201_CREATED)
        return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwawrgs):
        photo = Image.objects.get(uuid=request.GET['uuid'])
        try:
            like = Like.objects.get(photo=photo, ip_address=request.GET['ip_address'])
        except Like.DoesNotExist:
            like = None
        if like is not None:
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            Like.objects.get(**request.data).delete()
            return Response(status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            ...
        return Response(status.HTTP_304_NOT_MODIFIED)
