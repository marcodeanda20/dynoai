# Generated by Django 4.1.1 on 2023-02-05 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dyno', '0006_alter_imageupload_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
