from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/personal", views.personalProfile, name="personalProfile"),
    path("profile/project", views.projectProfile, name="projectProfile"),
    path("profile/donations", views.donationsProfile, name="donationsProfile"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
     path("activate/Resend-Email-Activation", views.reSendActivationMail, name="resendEmailActivation"),
]
