from django.shortcuts import render,redirect,get_object_or_404

from django.contrib import messages
from django.contrib.auth.models import User
# from .models import *
from .forms import *
# from .views import *


# Create your views here.
from  projects_app.models import Category, Projects

def home(request):
    cat_menu = Category.objects.all()
    last_5_projects = Projects.objects.order_by('-id')[:5]
    featured_projects = Projects.objects.filter(featured=True)[:5]
    

    print(last_5_projects)
    context = {
        'cat_menu': cat_menu,
        'last_5_projects': last_5_projects,
         'featured_projects': featured_projects
    }
    return render(request, 'home/home.html', context)
def get_category_projects(request, category_id):
   
        projects = Projects.objects.filter(
            category_id=category_id).all()

      
        title = Category.objects.get(id=category_id)
        context = {
            'title': title,
            'projects': projects,
          
        }
        return render(request, "home/category.html", context)
    

# def showProjects(request):   
#     context={'projects':Projects.objects.all()}
#     return render(request,'projects_app/project.html',context)


# def projectDetails(request,id):
#     project=Projects.objects.get(id=id)
#     photos= Image.objects.filter(project=project)
#     context={'project':project,'photos':photos}
#     return render(request,'projects_app/detail.html',context)
    

def category(request,foo):
    #replace Hyphenes with spaces
    foo=foo.replace('-','')
    # Grab the ccategory from the url 
    try:
        category=Category.objects.get(name=foo)
        projects=Projects.objects.filter(category=category)
        return render(request,'category.html',{'projects':projects,'category':category})
    except:
        messages.success(request,("That category doesn't exist"))
        return redirect('home')
        