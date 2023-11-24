from django.shortcuts import render,redirect
from django.views.generic import UpdateView,CreateView,DeleteView,ListView,DetailView
from .models import Members,Events
from .forms import MembersRegistrationForm,AddEventForm
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import datetime
# Create your views here.

class HomeView(ListView):
    model=Members
    template_name='members_dashboard.html'
  
class AddMembersView(CreateView):
    form_class=MembersRegistrationForm
    template_name='add_member.html'
    success_url=reverse_lazy('homepage')


    

class EditMemberProfile(UpdateView):
    model=Members
    fields='__all__'
    template_name='edit_member_profile.html'
    success_url=reverse_lazy('homepage')
class DeleteMember(DeleteView):
    model=Members
    template_name='delete_member.html'
    success_url=reverse_lazy('homepage')

class EventsView(ListView):
    model=Events
    template_name='events_dashboard.html'
    ordering=['-created_at']

class EventDetailView(DetailView):
    model=Events
    template_name='events_detail.html'



class AddEventsView(CreateView):
    model=Events
    template_name='add_events.html'
    form_class=AddEventForm
    success_url=reverse_lazy('events')

class DeleteEventsView(DeleteView):
    model=Events
    template_name='delete_events.html'
    success_url=reverse_lazy('events')
    



    
#add redirection



def search(request):
    if request.method=='POST':
        data=request.POST.get("search_user")
        member=Members.objects.filter(Q(username__icontains=data))
        if member:
            return render(request, 'search_member.html',{'member':member})
        else:
            return render(request, 'no_member.html')
    
    else:
            return render(request, 'members_dashboard.html')


def about_us(request):
    return render(request, 'About us.html')