# Generated by Django 4.1 on 2022-08-21 12:21

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_product_images_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='size',
            field=models.CharField(choices=[('32', '32'), ('34', '34'), ('36', '36'), ('38', '38'), ('40', '40'), ('42', '42'), ('44', '44'), ('46', '46'), ('Default', 'Default')], default='default', max_length=20, null=True),
        ),
    ]
