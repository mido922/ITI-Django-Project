# from django.contrib import admin
# from .models import *

# Register your models here.



from django.contrib import admin
from .models import Projects, Image

class ProjectImageInline(admin.StackedInline):
    model = Image

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

@admin.register(Image)
class ProjectImageAdmin(admin.ModelAdmin):
    pass
