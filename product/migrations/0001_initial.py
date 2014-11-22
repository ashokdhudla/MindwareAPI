# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import product.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(max_length=100, db_column=b'Brand_name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Product Name')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('image', models.FileField(upload_to=product.models.Content_files)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand_id', models.ForeignKey(to='product.brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='product_categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100, db_column=b'Category')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='cat_id',
            field=models.ForeignKey(to='product.product_categories'),
            preserve_default=True,
        ),
    ]
