from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    user_type = models.IntegerField()
    roles = models.CharField(max_length=250)
    status = models.CharField(max_length=20)

class Schedules(models.Model):
    name = models.CharField(max_length=250)
    weekly_day = models.IntegerField()
    level = models.IntegerField()
    start_hour = models.CharField(max_length=100)
    end_hour = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

class LogAccess(models.Model):
    level = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    request_type = models.CharField(max_length=10)
    date = models.DateTimeField()
