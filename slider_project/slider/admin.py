from django.contrib import admin
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer

from .models import SliderImage
from adminsortable2.admin import SortableAdminMixin


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'image', 'image_tag', 'order')

    def image_tag(self, obj):
        thumbnail = get_thumbnailer(obj.image).get_thumbnail({
            'size': (150, 150),
            'crop': True,
            'quality': 90
        })
        return format_html('<img src="{}"/>'.format(thumbnail.url))

    image_tag.short_description = 'Image'

