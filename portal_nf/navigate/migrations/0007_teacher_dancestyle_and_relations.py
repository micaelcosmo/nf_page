"""
# Add Teacher and DanceStyle models with relations

1. New Tables
  - Teacher
    - name (CharField)
    - bio (TextField) 
    - specialty (CharField)
    - photo_url (URLField)
    - active (BooleanField)
  
  - DanceStyle
    - name (CharField)
    - description (TextField)
    - level_description (TextField)

2. Changes
  - Add teacher and dance_style ForeignKey to Schedules
  - Add price field to Schedules
  - Add teacher and dance_style ForeignKey to ExperimentalClass

3. Security
  - No special security needed for these models
"""

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0006_experimentalclass_observations_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('bio', models.TextField()),
                ('specialty', models.CharField(max_length=100)),
                ('photo_url', models.URLField(max_length=500)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DanceStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('level_description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='schedules',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='navigate.teacher'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='dance_style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='navigate.dancestyle'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=10),
        ),
        migrations.AddField(
            model_name='experimentalclass',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='navigate.teacher'),
        ),
        migrations.AddField(
            model_name='experimentalclass',
            name='dance_style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='navigate.dancestyle'),
        ),
    ]