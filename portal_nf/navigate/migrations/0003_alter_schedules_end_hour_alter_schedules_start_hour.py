# Generated by Django 5.0.8 on 2024-08-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0002_rename_type_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='end_hour',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='start_hour',
            field=models.CharField(max_length=100),
        ),
    ]
