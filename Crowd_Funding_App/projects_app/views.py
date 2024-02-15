from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    CreateView,
)




def project_view(request):
   
    context={'projects':Projects.objects.all()}
    return render(request,'projects_app/project.html',context)


def detail_view(request,id):
    obj1=Projects.objects.get(id=id)
    photos= Image.objects.filter(project=obj1)
    context={'projects':obj1,'photos':photos}
    return render(request,'projects_app/detail.html',context)
    

# Create your views here.
@login_required
def addproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            images = request.FILES.getlist('images')
            for image in images:
                Image.objects.create(project=project, image=image)
            
        return redirect("home")
    else:
        form = ProjectForm()
        return render(request, 'projects_app/addproject.html', {'form': form})


# class projectAddgeneric(CreateView):
#     model=Projects
#     form_class=ProjectForm 
#     template_name='projects_app/addproject.html'
#     context_object_name = "form"  # context var name
#     success_url=reverse_lazy("home")
    

# class ImageAddgeneric(CreateView):
#     model=Image
#     form_class=ImageForm 
#     template_name='projects_app/addproject.html'
#     context_object_name = "form"  # context var name
#     success_url=reverse_lazy("home")
    

   