# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-04 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='teams',
            field=models.ManyToManyField(to='data.Team'),
        ),
    ]
