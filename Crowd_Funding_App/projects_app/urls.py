from django.urls import path
# from home_app import views
from . import views



urlpatterns = [
    # path('add', views.projectAddgeneric.as_view(), name="projects"),
    # path('add', views.ImageAddgeneric.as_view(), name="projects"),
    path("",views.project_view,name="project"),
    path("<int:id>/",views.detail_view,name="detail"),
    path("addproject/",views.addproject,name="addproject"),


]
