# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-22 19:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20160922_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Doctor', 'verbose_name_plural': 'Doctors'},
        ),
    ]