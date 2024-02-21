from django.db import models

# Create your models here.


from django.db import models


class SliderItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')


class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name