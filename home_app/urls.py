from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
 path('category/<int:category_id>', views.get_category_projects, name='get_category'),
    
]
