from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.core.validators import RegexValidator
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
        ]


class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(attrs={"placeholder": "ex : 01234567890"}),
        required=False,
        validators=[
            RegexValidator(
                regex=r"^(010|011|012|015)\d{8}$",
                message="Enter a valid phone number.",
            )
        ],
    )

    birthDate = forms.DateField(
        label="Birth Date",
        widget=forms.TextInput(attrs={"placeholder": "ex : Year-Month-Day"}),
        required=False,
    )

    faceBookAccount = forms.URLField(
        label="FaceBook Account",
        widget=forms.TextInput(attrs={"placeholder": "ex : https://example.com"}),
        required=False,
    )

    country = forms.CharField(
        label="Country",
        widget=forms.TextInput(attrs={"placeholder": "ex : Country"}),
        required=False,
    )

    class Meta:
        model = Profile
        # fields = "__all__"
        fields = ["phone", "birthDate", "faceBookAccount", "country", "image"]
