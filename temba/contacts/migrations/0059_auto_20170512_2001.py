# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0058_remove_contactgroup_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacturn',
            name='urn',
            field=models.CharField(choices=[('tel', 'Phone number'), ('facebook', 'Facebook identifier'), ('twitter', 'Twitter handle'), ('viber', 'Viber identifier'), ('line', 'LINE identifier'), ('telegram', 'Telegram identifier'), ('mailto', 'Email address'), ('ext', 'External identifier'), ('jiochat', 'Jiochat identifier'), ('fcm', 'Firebase Cloud Messaging identifier')], help_text='The Universal Resource Name as a string. ex: tel:+250788383383', max_length=255),
        ),
    ]
