# Generated by Django 5.0.3 on 2024-03-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_coursespeciality_coursesrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesrecord',
            name='image',
            field=models.ImageField(default=2, upload_to='media/library/courses'),
            preserve_default=False,
        ),
    ]
