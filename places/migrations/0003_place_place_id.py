# Generated by Django 4.1 on 2022-09-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image_image_image_image_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
