from django.contrib.auth.forms import AuthenticationForm
from django import forms
from CSEC_App.models import Members


class MemberLoginForm(AuthenticationForm):

    class Meta:
        model=Members
        fields=['email','password']

       