# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-07 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', '\u7537'), ('Female', '\u5973')], default='female', max_length=6),
        ),
    ]
