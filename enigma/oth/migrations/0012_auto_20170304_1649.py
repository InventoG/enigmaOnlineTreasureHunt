# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0011_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='images',
        ),
        migrations.AddField(
            model_name='question',
            name='images',
            field=models.ManyToManyField(to='oth.Image'),
        ),
    ]
