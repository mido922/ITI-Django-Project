import datetime
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def home(request):
    try:
        listOfFavoritedProjects=Project.objects.filter(favorited=True)
    except Project.DoesNotExist:
        listOfFavoritedProjects="None"

    try:
        listOfProjects=Project.objects.filter()
    except Project.DoesNotExist:
        listOfProjects="None"

    context={'projects':listOfProjects, 'favoriteProjects':listOfFavoritedProjects}
    templateName='home/home.html'


    return render(request, templateName, context)

def about(request):
    return render(request, "home/about.html")

def addAProject(request):
    if request.method == "POST":
       form=projectForm(request.POST, request.FILES)
       if(form.is_valid()):
        Project.objects.create(projectName=request.POST['projectName'],
                               projectTarget=request.POST['projectTarget'],
                               endDate=request.POST['endDate'],
                               username=request.user,
                               startDate=datetime.date.today(),
                               currentFunds=0,
                               )
        return render(request, "home/projectAddSuccess.html")
    else:
        form = projectForm
        return render(request, "home/addAProject.html", {"form": form})


def showProjectPage(request, projectID):
    selectedProject=Project.objects.get(id=projectID)
    try:
        listOfComments=Comment.objects.filter(projectID=projectID)
    except Comment.DoesNotExist:
        listOfComments="None"
    context={'project':selectedProject, 'commentForm':commentForm, 'listOfComments':listOfComments, 'donationForm':donationForm}
    return render(request, 'home/projectDetails.html', context)

def addAComment(request,projectID):
    form=commentForm(request.POST, request.FILES)
    if(form.is_valid()):
        Comment.objects.create(commentContent=request.POST['commentContent'],
                               projectID=projectID,
                               username=request.user,
                               commentDate=datetime.date.today(),  
                               reported=False 
                               )
        
        return render(request, "home/commentAddSuccess.html")
    
def addADonation(request,projectID):
    form=donationForm(request.POST)
    oldValue = Project.objects.get(id=projectID).currentFunds
    newValue = oldValue + float(request.POST['donationAmount'])
    if form.is_valid():
        Project.objects.filter(id=projectID).update(currentFunds = newValue)
        Donation.objects.create(donationAmount=request.POST['donationAmount'],
                               projectID=projectID,
                               username=request.user,  
                               )

        return render(request, "home/testPage.html")
    
def checkYourDonations(request):
    try:
        listOfDonations=Donation.objects.filter(username=request.user)
    except Donation.DoesNotExist:
        listOfComments="None"

    context={'listOfDonations':listOfDonations}
    return render(request, 'home/yourDonations.html', context)