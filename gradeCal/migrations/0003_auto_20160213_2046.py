# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradeCal', '0002_Changed some Entity field names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='max_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='course',
            name='assignment_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='homework_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='test_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='homework',
            name='max_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='homework',
            name='score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='test',
            name='max_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='test',
            name='score',
            field=models.FloatField(default=0.0),
        ),
    ]
