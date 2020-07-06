from images.models import Image


def update_images():
    Image.objects.filter(show_later=True).update(show_later=False)