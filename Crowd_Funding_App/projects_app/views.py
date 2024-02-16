from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def showProjects(request):   
    context={'projects':Projects.objects.all()}
    return render(request,'projects_app/project.html',context)


def projectDetails(request,id):
    project=Projects.objects.get(id=id)
    photos= Image.objects.filter(project=project)
    context={'project':project,'photos':photos}
    return render(request,'projects_app/detail.html',context)
    

# Create your views here.
@login_required
def addProject(request):
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