# Generated by Django 4.1 on 2024-11-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0004_alter_sliderimage_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]