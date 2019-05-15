import datetime
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.db import models




class Status(models.Model):
    status_name = models.CharField(max_length=100)
    status_color = models.CharField(max_length=9)


class Expert(models.Model):
    status = models.CharField(max_length=200)
    user = models.ForeignKey(User ,on_delete=models.CASCADE)



class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    duration = models.IntegerField
    created_at = models.DateTimeField(default=datetime.datetime.now())
    created_by = models.ForeignKey(Expert, on_delete=models.CASCADE, blank=True, null=True)


class Assignee(models.Model):
    phoneNumber = models.CharField(max_length=200)
    bin = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    rating = models.FloatField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task)


class BecomeAssigneeRequest(models.Model):
    phoneNumber = models.CharField(max_length=200)
    bin = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    isJudged = models.BooleanField
    essay = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

