# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-28 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0071_auto_20160428_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Person'),
        ),
    ]
