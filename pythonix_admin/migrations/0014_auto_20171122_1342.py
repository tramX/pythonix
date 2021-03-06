# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-22 13:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pythonix_admin', '0013_auto_20171122_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='end_used_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 25, 13, 42, 50, 607924), verbose_name='Дата окончяния услуги'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='select_street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pythonix_admin.Streets', verbose_name='Выбор улицы'),
        ),
        migrations.AlterField(
            model_name='temporarypay',
            name='del_pay',
            field=models.DateField(default=datetime.datetime(2017, 11, 25, 13, 42, 50, 612901), verbose_name='Дата удаления временного платежа'),
        ),
    ]
