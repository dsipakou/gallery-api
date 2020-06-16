from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from images.models import Image, Like
from images.serializers import ImageSerializer, LikeSerializer


class ImageListView(ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(show_later=False).order_by("date_created").reverse()[:6]

    def list(self, request, *args, **kwargs):
        return super().list(request, **kwargs)


class ImageView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = "uuid"

    def retrieve(self, request, *args, **kwargs):
        image = self.get_object()
        return Response(self.get_serializer(image).data)


class HotImageView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request):
        images = self.queryset.filter(show_later=True)
        return Response(self.get_serializer(images[0]).data)


class LikeView(GenericViewSet):
    serializer_class = LikeSerializer

    def post(self, request, **kwargs):
        data = request.data
        data['ip_address'] = request.META['REMOTE_ADDR']
        like = Like.objects.filter(**data)
        if len(like) == 0:
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_304_NOT_MODIFIED)

    def get(self, request, **kwargs):
        photo = Image.objects.get(uuid=kwargs.get('uuid'))
        try:
            like = Like.objects.get(photo=photo, ip_address=request.META['REMOTE_ADDR'])
        except Like.DoesNotExist:
            like = None
        if like is not None:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request):
        try:
            Like.objects.get(**request.data).delete()
        except Like.DoesNotExist:
            ...
        finally:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_304_NOT_MODIFIED)
