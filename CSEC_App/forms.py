
from django.db import models
from .models import Members,Events
from django.contrib.auth.forms import UserCreationForm
from django import forms

class MembersRegistrationForm(UserCreationForm):
    
    class Meta:
        model=Members
        fields=['username','first_name','last_name','email','department','profile_pic','Roll','profile_pic','password1','password2','is_staff']
    
    

class AddEventForm(forms.ModelForm):

    class Meta:
        model=Events
        fields=['title','description','date','time','venue','organizer']

