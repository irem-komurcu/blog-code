# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-03 14:05
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20180302_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Content'),
        ),
    ]
