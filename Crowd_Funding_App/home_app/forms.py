from django import forms


class projectForm(forms.Form):
    projectName = forms.CharField()
    projectTarget = forms.FloatField()
    endDate = forms.DateField()

class commentForm(forms.Form):
    commentContent = forms.CharField(label="Leave a comment!")

class donationForm(forms.Form):
    donationAmount = forms.IntegerField(label="How much would you like to donate?")