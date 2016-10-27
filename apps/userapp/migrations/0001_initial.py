# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=50)),
                ('apt', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('code', models.CharField(max_length=6)),
                ('valid', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
                ('address', models.ManyToManyField(related_name='useraddress', to='userapp.Address')),
            ],
        ),
    ]