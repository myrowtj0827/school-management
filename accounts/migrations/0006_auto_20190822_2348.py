# Generated by Django 2.2.3 on 2019-08-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('student', 'SchoolStudent'), ('teacher', 'Teacher'), ('school', 'School'),
                                            ('curator', 'Curator'), ('editor', 'Editor'),
                                            ('super admin', 'Super Admin')], max_length=11,
                                   verbose_name='Account Type'),
        ),
    ]
