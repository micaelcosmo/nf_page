from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    user_type = models.IntegerField()
    roles = models.CharField(max_length=250)
    status = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField()
    specialty = models.CharField(max_length=100)
    photo_url = models.URLField(max_length=500)
    active = models.BooleanField(default=True)

class DanceStyle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level_description = models.TextField()

class Schedules(models.Model):
    name = models.CharField(max_length=250)
    weekly_day = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    start_hour = models.CharField(max_length=100)
    end_hour = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    dance_style = models.ForeignKey(DanceStyle, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class LogAccess(models.Model):
    level = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    request_type = models.CharField(max_length=10)
    date = models.CharField(max_length=100)

class ExperimentalClass(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    weekly_day = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    start_hour = models.CharField(max_length=100)
    end_hour = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Agendado')
    observations = models.CharField(max_length=500, default='')
    dance_style = models.ForeignKey(DanceStyle, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)