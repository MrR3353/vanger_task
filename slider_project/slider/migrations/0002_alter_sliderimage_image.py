# Generated by Django 4.1 on 2024-11-28 18:47

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_images', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
