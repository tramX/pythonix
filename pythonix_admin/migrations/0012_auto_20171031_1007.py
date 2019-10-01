# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 10:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonix_admin', '0011_auto_20171018_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='end_used_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 3, 10, 7, 23, 435489), verbose_name='Дата окончяния услуги'),
        ),
        migrations.AlterField(
            model_name='sendemailadmin',
            name='event',
            field=models.CharField(choices=[('new_month', 'new_month'), ('clients_off', 'clients_off'), ('celery_on', 'celery_on'), ('payment', 'payment'), ('deferred_actions', 'Отложенные действия')], max_length=255),
        ),
        migrations.AlterField(
            model_name='temporarypay',
            name='del_pay',
            field=models.DateField(default=datetime.datetime(2017, 11, 3, 10, 7, 23, 439962), verbose_name='Дата удаления временного платежа'),
        ),
    ]
