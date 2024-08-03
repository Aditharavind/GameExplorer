from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserPCSpec, Review

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserPCSpecForm(forms.ModelForm):
    class Meta:
        model = UserPCSpec
        fields = ["cpu", "gpu", "ram", "storage", "os_version"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
