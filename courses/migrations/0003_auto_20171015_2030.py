# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-16 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_step'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
