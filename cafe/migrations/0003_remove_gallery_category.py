# Generated by Django 4.0.3 on 2022-04-23 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_alter_cafeinfo_logo_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='category',
        ),
    ]
