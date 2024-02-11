from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authViews
from . import views

from .views import *

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
