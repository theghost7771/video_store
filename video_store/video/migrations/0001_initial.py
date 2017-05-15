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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('is_available', models.BooleanField(verbose_name='Is available', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
