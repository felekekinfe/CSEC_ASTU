from django.urls import path
from .views import HomeView,AddMembersView,AddEventsView,EventsView,EventDetailView,DeleteMember,DeleteEventsView

urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('add_member/',AddMembersView.as_view(),name='addmember'),
    path('add_event',AddEventsView.as_view(),name='addevent'),
    path('up_comming_event',EventsView.as_view(),name='events'),
    path('event_detail/<int:pk>',EventDetailView.as_view(),name='eventdetail'),
    path('delete_member/<int:pk>',DeleteMember.as_view(),name='deletemember'),
    path('delet_events/<int:pk>',DeleteEventsView.as_view(),name='deleteevents')




]