from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields='__all__'
    

#category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'