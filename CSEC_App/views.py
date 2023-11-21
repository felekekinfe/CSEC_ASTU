from django.shortcuts import render
from django.views.generic import UpdateView,CreateView,DeleteView,ListView,DetailView
from .models import Members

# Create your views here.

class HomeView(ListView):
    model=Members
    template_name='members_dashboard.html'
    


