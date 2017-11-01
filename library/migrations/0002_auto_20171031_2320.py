# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='book',
            name='seller',
            field=models.CharField(default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='null', max_length=20),
        ),
    ]