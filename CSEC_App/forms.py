
from django.db import models
from .models import Members,Events
from django.contrib.auth.forms import UserCreationForm
from django import forms

class MembersRegistrationForm(UserCreationForm):
    
    class Meta:
        model=Members
        fields=['first_name','last_name','email','department','Roll','password1','password2']
    


class AddEventForm(forms.ModelForm):

    class Meta:
        model=Events
        fields=['title','description','date','time','venue','organizer']

