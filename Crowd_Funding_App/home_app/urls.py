from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("addAProject", views.addAProject, name="addAProject"),
    path("yourDonations/", views.checkYourDonations, name="checkYourDonations"),
    path("project/addAComment/<int:projectID>", views.addAComment, name="addAComment"),
    path("project/addACommentReport/<int:commentID>", views.addACommentReport, name="addACommentReport"),
    path("project/addAProjectReport/<int:projectID>", views.addAProjectReport, name="addAProjectReport"),
    path("project/cancelYourProject/<int:projectID>", views.cancelYourProject, name="cancelYourProject"),
    path("project/addADonation/<int:projectID>", views.addADonation, name="addADonation"),
    path("project/addARating/<int:projectID>/<int:rating>", views.addARating, name="addARating"),
]