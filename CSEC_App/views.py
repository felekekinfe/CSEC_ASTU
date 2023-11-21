from django.shortcuts import render
from django.views.generic import UpdateView,CreateView,DeleteView,ListView,DetailView
from .models import Members,Events
from .forms import MembersRegistrationForm

# Create your views here.

class HomeView(ListView):
    model=Members
    template_name='members_dashboard.html'
class EventsView(ListView):
    model=Events
    template_name='events_dashboard.html'
class EventDetailView(DetailView):
    model=Events
    template_name='events_detail.html'

class AddMembersView(CreateView):
    model=Members
    form_class=MembersRegistrationForm
    template_name='add_member.html'

class AddEventsView(CreateView):
    model=Events
    template_name='add_events.html'
    fields='__all__'

class DeleteMember(DeleteView):
    model=Members
    template_name='delete_member.html'
    



    



