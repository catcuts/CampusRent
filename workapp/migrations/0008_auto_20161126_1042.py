# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0007_auto_20161125_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yytime', models.DateField(auto_now=True)),
                ('yyname', models.CharField(blank=True, max_length=200)),
                ('yyphone', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='houseinfo',
            name='housetype',
            field=models.CharField(blank=True, choices=[('三室一厅一卫', '三室一厅一卫'), ('二室一厅一卫', '二室一厅一卫'), ('三室两厅两卫', '三室两厅两卫'), ('三室一厅两卫', '三室一厅两卫'), ('一室一厅一卫', '一室一厅一卫'), ('四室两厅两卫', '四室两厅两卫')], max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女'), ('保密', '保密')], default='保密', max_length=10),
        ),
    ]