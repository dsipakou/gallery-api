from django.contrib import admin

from images.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('admin_image_tag', 'name', 'date_created', 'date_updated')
    readonly_fields = ['uuid']

admin.site.register(Image, ImageAdmin)
