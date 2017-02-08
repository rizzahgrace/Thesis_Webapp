# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 07:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawData_AMPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid', models.FloatField(null=True)),
                ('load', models.FloatField(null=True)),
                ('batt_curr', models.FloatField(null=True)),
                ('batt_volt', models.FloatField(null=True)),
                ('SP_curr', models.FloatField(null=True)),
                ('SP_volt', models.FloatField(null=True)),
                ('SP_pow', models.FloatField(null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date logged')),
                ('AMPS_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='RawData',
            new_name='RawData_Weather',
        ),
    ]
