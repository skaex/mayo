# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 10:51
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20170615_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='prequest',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='prequest',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
