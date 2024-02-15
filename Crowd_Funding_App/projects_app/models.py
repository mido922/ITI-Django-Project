from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Projects(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    total_target = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(blank=True)  
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(Projects, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_images/")
    def getImageUrl(self):
        return f"/media/{self.image}"

# class Tag(models.Model):
#     name = models.TextField(max_length=50)
#     project = models.ForeignKey(Projects, default=None, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.project.title