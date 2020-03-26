# Generated by Django 2.2.3 on 2019-09-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0009_auto_20190902_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='account_type',
            field=models.CharField(
                choices=[('student', 'SchoolStudent'), ('aonestudent', 'Student'), ('teacher', 'Teacher'),
                         ('school', 'School'), ('curator', 'Curator'), ('editor', 'Editor'),
                         ('super admin', 'Super Admin'), ('admin', 'Admin')], max_length=11,
                verbose_name='Account Type'),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(
                choices=[('student', 'SchoolStudent'), ('aonestudent', 'Student'), ('teacher', 'Teacher'),
                         ('school', 'School'), ('curator', 'Curator'), ('editor', 'Editor'),
                         ('super admin', 'Super Admin'), ('admin', 'Admin')], max_length=11,
                verbose_name='Account Type'),
        ),
    ]
