import uuid
import shortuuid

from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToCover
from django.utils.translation import ugettext_lazy as _


class Image(models.Model):
    uuid = models.CharField(_('image uuid'), max_length=36, null=True, blank=True)
    photo = ProcessedImageField(verbose_name=_('photo'),
                                upload_to='uploads/gallery/images',
                                processors=[ResizeToFit(1920, 1080)],
                                format='PNG')
    photo_preview = ImageSpecField(source='photo',
                                   processors=[ResizeToCover(250, 250)],
                                   format='PNG')
    name = models.CharField(_('name'), max_length=80, blank=False)
    description = models.TextField(_('description'), max_length=8000, blank=True)
    date_created = models.DateTimeField(_('date created'), auto_created=True, auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    def __str__(self):
        return self.name

    def admin_image_tag(self):
        return mark_safe('<img src="{}" />'.format(self.photo_preview.url))

    admin_image_tag.short_desription = _('image short desc')

@receiver(signals.pre_save, sender=Image)
def set_uuid_for_image(sender, instance=None, **kwargs):
    if instance and not instance.uuid:
        instance.uuid = shortuuid.encode(uuid.uuid4())
        instance.save()
