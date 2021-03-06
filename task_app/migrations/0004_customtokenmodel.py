# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('task_app', '0003_auto_20170726_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTokenModel',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.Token')),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'custom_token_model',
            },
            bases=('authtoken.token',),
        ),
    ]
