# Generated by Django 4.1.1 on 2023-02-05 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyno', '0002_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='dyno/images/')),
            ],
        ),
    ]