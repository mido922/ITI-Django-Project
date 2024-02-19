from django.contrib import admin

# Register your models here.
from .models import Projects
from .models import Category

admin.site.register(Projects)
admin.site.register(Category)