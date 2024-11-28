from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = FilerImageField(related_name='slider_images', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)  # Поле для сортировки

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or "Image {}".format(self.pk)
