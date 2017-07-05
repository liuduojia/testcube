# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 08:58
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('path', models.CharField(max_length=2000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files',
                                             to='core.TestResult')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RunSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('run', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.TestRun')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]