# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('cuisine', models.CharField(max_length=255)),
                ('services', models.CharField(max_length=255)),
                ('drange', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
