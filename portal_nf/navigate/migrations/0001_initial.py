# Generated by Django 5.0.8 on 2024-08-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('request_type', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('weekly_day', models.IntegerField()),
                ('level', models.IntegerField()),
                ('start_hour', models.DateTimeField()),
                ('end_hour', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('type', models.IntegerField()),
                ('roles', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
