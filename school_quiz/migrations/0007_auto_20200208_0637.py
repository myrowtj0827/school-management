# Generated by Django 2.2.3 on 2020-02-07 22:37

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('school_quiz', '0006_auto_20200130_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprogress',
            name='score',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Score'),
        ),
        migrations.AlterField(
            model_name='historicalsitting',
            name='incorrect_questions',
            field=models.CharField(blank=True, max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Incorrect questions'),
        ),
        migrations.AlterField(
            model_name='historicalsitting',
            name='question_list',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Question List'),
        ),
        migrations.AlterField(
            model_name='historicalsitting',
            name='question_order',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Question Order'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='score',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Score'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='incorrect_questions',
            field=models.CharField(blank=True, max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Incorrect questions'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_list',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Question List'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_order',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Question Order'),
        ),
    ]
