# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import promotions.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='promotions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promo_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('image', models.FileField(upload_to=promotions.models.Content_files)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
