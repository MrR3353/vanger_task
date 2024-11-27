from django.db import models


class SliderImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='slider_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title or "Image {}".format(self.pk)
