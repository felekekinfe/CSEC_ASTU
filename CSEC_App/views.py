from django.shortcuts import render
from django.views.generic import UpdateView,CreateView,DeleteView,ListView,DetailView
from .models import Members
from .forms import MembersRegistrationForm

# Create your views here.

class HomeView(ListView):
    model=Members
    template_name='members_dashboard.html'

class AddMembersView(CreateView):
    model=Members
    form_class=MembersRegistrationForm
    template_name='add_member.html'



