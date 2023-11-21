from django.shortcuts import render
from django.contrib.auth.views import LoginView
from CSEC_App.models import Members
from .forms import MemberLoginForm
from django.urls import reverse_lazy

# Create your views here.

class MembersLoginView(LoginView):
    template_name='login_member.html'
    form_class=MemberLoginForm
    success_url=reverse_lazy('homepage')

    def get_success_url(self):
        return self.success_url
    #add redirection
