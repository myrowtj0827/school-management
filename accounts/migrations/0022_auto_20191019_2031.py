# Generated by Django 2.2.3 on 2019-10-20 03:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0021_auto_20191019_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curator',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curator',
                                    to='accounts.SuperAdmin'),
        ),
        migrations.AlterField(
            model_name='curator',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='curator',
                                       to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='editor',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor',
                                    to='accounts.SuperAdmin'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='editor',
                                       to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marketer',
            name='admin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='marketer',
                                    to='accounts.SuperAdmin'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marketer',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='marketer_profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='open_student_profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='superadmin',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='super_admin_profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
