# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_auto_20170131_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/none/default_avatar.jpg', upload_to='avatars/'),
        ),
    ]
