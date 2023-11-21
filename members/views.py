from django.shortcuts import render
from django.contrib.auth.views import LoginView
from CSEC_App.models import Members
from .forms import MemberLoginForm
# Create your views here.

class MembersLoginView(LoginView):
    model=Members
    template_name='login_member.html'
    form_class=MemberLoginForm

    #add redirection
