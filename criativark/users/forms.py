from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class CreateAccForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        
        
class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "contact", "bio", "image"]
        exclude = ["user"]
        label ={
            "image":"chose avatar"
        }
        
