# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_input_path', models.FileField(upload_to='/home/gongxijun/data/upload_image')),
                ('_output_path', models.FileField(upload_to='/home/gongxijun/data/result_image')),
            ],
        ),
    ]