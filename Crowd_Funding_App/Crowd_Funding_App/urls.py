"""
URL configuration for Crowd_Funding_App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import *
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings
from user_auth_app import views as authViews
from user_auth_app.views import CustomLoginView

urlpatterns = [
    path("", include("home_app.urls")),
    path("user/", include("user_auth_app.urls")),
    path("accounts/login/", CustomLoginView.as_view(),name="login"),    
    path("admin/", admin.site.urls),
    path("project/", include("projects_app.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
