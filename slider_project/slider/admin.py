from django.contrib import admin
from django.utils.html import format_html

from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'image_tag')

    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

