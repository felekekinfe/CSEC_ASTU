from django.urls import path
from .views import HomeView,AddMembersView,AddEventsView,EventsView,EventDetailView

urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('add_member/',AddMembersView.as_view(),name='addmember'),
    path('add_event',AddEventsView.as_view(),name='addevent'),
    path('up_comming_event',EventsView.as_view(),name='events'),
    path('eventdetail/<int:pk>',EventDetailView.as_view(),name='eventdetail')



]