# Generated by Django 4.1 on 2024-11-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_alter_sliderimage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
