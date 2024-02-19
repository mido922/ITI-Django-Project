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
    elif not request.user.is_authenticated:
        context={'errorMessage':"You are not authorized to start new projects."}
        return render(request, 'home/errorPage.html', context)
    else:
        form = projectForm
        return render(request, "home/addAProject.html", {"form": form})

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

def showProjectPage(request, projectID):
    selectedProject=Project.objects.get(id=projectID)
    try:
        listOfComments=Comment.objects.filter(projectID=projectID)
    except Comment.DoesNotExist:
        listOfComments="None"

    #Start Ratings Block

    ratings=Rating.objects.all().filter(projectID=projectID)

    print(ratings)

    totalRating = 0
    numberOfRatings = 0
    averageRating = 0

    for i in range(len(ratings)):
        totalRating += ratings[i].ratingValue
        numberOfRatings+=1
        averageRating = totalRating/numberOfRatings

    #End Ratings Block
        
    #Start Tags Block
    tags=Tag.objects.all().filter(projectID=projectID)

    print(tags)

    for i in range(len(tags)):
        similarProjects=Project.objects.all().filter(projectID=projectID)

    #End Tags Block
    
    context={
        'project':selectedProject,
        'commentForm':commentForm,
        'listOfComments':listOfComments,
        'donationForm':donationForm,
        'rating':averageRating,
        'tags':tags,
        }
    return render(request, 'home/projectDetails.html', context)

def cancelYourProject(request, projectID):
    selectedProject = selectedProject=Project.objects.get(id=projectID)
    print (request.user, selectedProject.username)

    if not (request.user == selectedProject.username):
        context={'errorMessage':"You are not authorized to delete this project."}
        return render(request, 'home/errorPage.html', context)
    
    if selectedProject.currentFunds > (0.25*selectedProject.projectTarget):
        context={'errorMessage':"You cannot delete a project while it is over 25 percent funded."}
        return render(request, 'home/errorPage.html', context)
    
    # selectedProject.delete()
    print("It would have been deleted!")
    context={'successMessage':"Project Successfully Deleted."}
    return render(request, 'home/successPage.html', context)

def addACommentReport(request,commentID):

    if CommentReport.objects.filter(commentID=commentID).filter(username=request.user).exists():
        CommentReport.objects.filter(commentID=commentID).filter(username=request.user).delete()
    else:
        CommentReport.objects.create(
        commentID=commentID,
        username=request.user,
        )

    context={'successMessage':"Report Successfully Added or Removed."}
    return render(request, 'home/successPage.html', context)

def addAProjectReport(request,projectID):

    if ProjectReport.objects.filter(projectID=projectID).filter(username=request.user).exists():
        ProjectReport.objects.filter(projectID=projectID).filter(username=request.user).delete()
    else:
        ProjectReport.objects.create(
        projectID=projectID,
        username=request.user,
        )

    context={'successMessage':"Report Successfully Added or Removed."}
    return render(request, 'home/successPage.html', context)

def addARating(request,projectID,rating):
    if Rating.objects.filter(projectID=projectID).filter(username=request.user).exists():
        Rating.objects.filter(projectID=projectID).filter(username=request.user).delete()
    else:
        Rating.objects.create(
        projectID=projectID,
        username=request.user,
        ratingValue=rating
        )

    context={'successMessage':"Successfully Added or Removed your rating."}
    return render(request, 'home/successPage.html', context)