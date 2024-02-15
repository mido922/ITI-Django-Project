from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
   
    class Meta:
        model=Projects
        fields='__all__'
        
        def clean_name(self):
            enteredname=self.cleaned_data['name']
            obj=Projects.objects.get(name=enteredname).exists()
            if obj:
                raise ValidationError('name must be unique')
            else:
                return True


        
#category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        def clean_name(self):
            enteredname=self.cleaned_data['name']
            obj=Category.objects.get(name=enteredname).exists()
            if obj:
                raise ValidationError('name must be unique')
            else:
                return True                

# Image form
# class ImageForm(forms.Form):
#     class Meta:
#         model=Image
#         fields='__all__'

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model=Image
#         fields='__all__'
        

# class TagForm(forms.ModelForm):
#     class Meta:
#         model=Tag
#         fields='__all__'
#         def clean_name(self):
#             enteredname=self.cleaned_data['name']
#             obj=Tag.objects.get(name=enteredname).exists()
#             if obj:
#                 raise ValidationError('name must be unique')
#             else:
#                 return True
