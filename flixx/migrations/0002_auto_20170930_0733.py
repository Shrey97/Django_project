# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-30 07:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flixx', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='DateOfBirth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Headshot',
        ),
    ]