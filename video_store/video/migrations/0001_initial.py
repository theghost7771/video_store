# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('aviable', models.BooleanField(default=True, verbose_name='Is aviable')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
