# Generated by Django 3.1.2 on 2020-10-21 17:10

from django.db import migrations, models
import ventas.models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20201021_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='img_product',
            field=models.ImageField(blank=True, upload_to=ventas.models.upload_to, verbose_name='img_product'),
        ),
    ]
