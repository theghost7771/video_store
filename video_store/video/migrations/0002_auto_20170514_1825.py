# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def create_initial_data(apps, schema_editor):
    Video = apps.get_model("video", "Video")
    Video.objects.bulk_create([Video(title='Title {}'.format(number)) for number in range(1, 11)])


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
