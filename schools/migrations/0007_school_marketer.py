# Generated by Django 2.2.3 on 2019-10-10 04:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0019_auto_20191009_2136'),
        ('schools', '0006_auto_20190923_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='marketer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schools',
                                    to='accounts.Marketer'),
        ),
    ]
