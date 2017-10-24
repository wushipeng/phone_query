# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-06 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='员工姓名')),
                ('pyjc', models.CharField(max_length=6, verbose_name='员工姓名简称')),
                ('phone_number', models.IntegerField(verbose_name='分机号码')),
                ('part', models.CharField(max_length=60, verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='RegionalPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=32, verbose_name='分公司所在城市名称')),
                ('phone_number', models.CharField(max_length=16, verbose_name='电话号码')),
            ],
        ),
    ]