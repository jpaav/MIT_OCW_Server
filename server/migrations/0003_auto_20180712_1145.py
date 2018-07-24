# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-12 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_course_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='asTaughtIn',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructors',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='readings',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='coursediscipline',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]