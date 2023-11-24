
from django.db import models
from .models import Members,Events
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Members

class MembersRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    department = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'})
    )
    Roll = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Roll'})
    )
    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )
    password1 = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(label='Confirm password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password','lables':'con'})
    )
    is_staff = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Members
        fields = ['first_name', 'last_name', 'email', 'department', 'Roll', 'profile_pic', 'password1', 'password2', 'is_staff']




class AddEventForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'})
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Time'}),
        input_formats=['%H:%M', '%I:%M %p']
    )
    venue = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue'})
    )
    organizer = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CSEC_Dev'})
    )

    class Meta:
        model = Events
        fields = ['title', 'description', 'date', 'time', 'venue', 'organizer']
