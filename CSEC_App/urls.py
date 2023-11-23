from django.urls import path
from .views import about_us,search,HomeView,AddMembersView,AddEventsView,EventsView,EventDetailView,DeleteMember,DeleteEventsView,EditMemberProfile

urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('add_member/',AddMembersView.as_view(),name='addmember'),
    path('add_event',AddEventsView.as_view(),name='addevent'),
    path('up_comming_event',EventsView.as_view(),name='events'),
    path('event_detail/<int:pk>',EventDetailView.as_view(),name='eventdetail'),
    path('delete_member/<int:pk>',DeleteMember.as_view(),name='deletemember'),
    path('edit_member/<int:pk>',EditMemberProfile.as_view(),name='editmember'),
    path('delet_events/<int:pk>',DeleteEventsView.as_view(),name='deleteevents'),

    path('search_member',search,name='search_member'),
    path('about_us',about_us,name='aboutus'),


]