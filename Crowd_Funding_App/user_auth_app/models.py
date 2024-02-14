from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.utils import timezone


class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=100,
        default="01234567890",
        null=True,
    )
    birthDate = models.DateField(
        default=timezone.now,
        null=True,
    )
    faceBookAccount = models.URLField(
        default="https://example.com",
        null=True,
    )
    country = models.CharField(
        max_length=100,
        default="Country",
        null=True,
    )
    image = models.ImageField(
        default="default.png",
        upload_to="profile_picture",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()