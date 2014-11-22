# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quiz_name', models.CharField(max_length=200)),
                ('from_date', models.DateTimeField(verbose_name=b'From_date')),
                ('to_date', models.DateTimeField(verbose_name=b'To_date')),
                ('no_of_questions', models.IntegerField(verbose_name=b'No_of_questions')),
                ('no_of_games_for_a_day', models.CharField(max_length=20, verbose_name=b'No_of_games_for_a_day')),
                ('min_score', models.IntegerField(verbose_name=b'Min_score')),
                ('active_status', models.IntegerField(verbose_name=b'Active_status')),
                ('points_correct', models.IntegerField(verbose_name=b'Points_correct')),
                ('points_wrong', models.IntegerField(verbose_name=b'Points_wrong')),
                ('points_three_correct', models.IntegerField(verbose_name=b'Points_three_correct')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
