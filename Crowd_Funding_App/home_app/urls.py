from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("addAProject", views.addAProject, name="addAProject"),
    path("project/addAComment/<int:projectID>", views.addAComment, name="addAComment"),
    # path("project/addAReport/<int:commentID>", views.addAReport, name="addAReport"),
    path("project/addADonation/<int:projectID>", views.addADonation, name="addADonation"),
    path("yourDonations/", views.checkYourDonations, name="checkYourDonations"),
]