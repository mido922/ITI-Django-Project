from django.db import models

# Create your models here.

class Comment(models.Model):
    projectID = models.IntegerField()
    username = models.CharField()
    commentContent = models.CharField()
    commentDate = models.DateField()
    reported = models.BooleanField()

class Project(models.Model):
    username = models.CharField()
    startDate = models.DateField()

    projectName = models.CharField()
    projectCategory = models.CharField()
    currentFunds = models.FloatField()
    projectTarget = models.FloatField()
    endDate = models.DateField()
    favorited = models.BooleanField()

class ProjectImage(models.Model):
    projectID = models.IntegerField()

class Report(models.Model):
    commentID = models.CharField()
    username = models.CharField()

class Donation(models.Model):
    projectID = models.IntegerField()
    username = models.CharField()
    donationAmount = models.FloatField()