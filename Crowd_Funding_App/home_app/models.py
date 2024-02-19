from django.db import models

# Create your models here.

class Comment(models.Model):
    projectID = models.IntegerField()
    username = models.CharField()
    commentContent = models.CharField()
    commentDate = models.DateField()
    reported = models.BooleanField(default=False)

class Project(models.Model):
    username = models.CharField()
    startDate = models.DateField()

    projectName = models.CharField()
    projectCategory = models.CharField()
    currentFunds = models.FloatField(default=0)
    projectTarget = models.FloatField()
    endDate = models.DateField()
    favorited = models.BooleanField()

class ProjectImage(models.Model):
    projectID = models.IntegerField()

class CommentReport(models.Model):
    commentID = models.CharField()
    username = models.CharField()

class ProjectReport(models.Model):
    projectID = models.CharField()
    username = models.CharField()

class Donation(models.Model):
    projectID = models.IntegerField()
    username = models.CharField()
    donationAmount = models.FloatField()

class Rating(models.Model):
    projectID = models.CharField()
    username = models.CharField()
    ratingValue = models.IntegerField()

class Tag(models.Model):
    projectID = models.IntegerField()
    tagContent = models.CharField()