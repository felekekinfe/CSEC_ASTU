from django.shortcuts import render
from django.views.generic import UpdateView,CreateView,DeleteView,ListView,DetailView
from .models import Members,Events
from .forms import MembersRegistrationForm,AddEventForm

# Create your views here.

class HomeView(ListView):
    model=Members
    template_name='members_dashboard.html'

class AddMembersView(CreateView):
    model=Members
    form_class=MembersRegistrationForm
    template_name='add_member.html'

class EditMemberProfile(UpdateView):
    model=Members
    fields='__all__'
    template_name='edit_member_profile.html'
class DeleteMember(DeleteView):
    model=Members
    template_name='delete_member.html'

class EventsView(ListView):
    model=Events
    template_name='events_dashboard.html'

class EventDetailView(DetailView):
    model=Events
    template_name='events_detail.html'



class AddEventsView(CreateView):
    model=Events
    template_name='add_events.html'
    form_class=AddEventForm

class DeleteEventsView(DeleteView):
    model=Events
    template_name='delete_events.html'
    



    
#add redirection


