# Generated by Django 5.0.8 on 2024-09-05 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0005_experimentalclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentalclass',
            name='observations',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='experimentalclass',
            name='status',
            field=models.CharField(default='Agendado', max_length=20),
        ),
    ]
