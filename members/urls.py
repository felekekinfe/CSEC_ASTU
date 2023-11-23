
from django.urls import path
from .views import MembersLoginView,UserProfileView

urlpatterns = [
    path('login/',MembersLoginView.as_view(),name='login'),
    path('Profile/<int:pk>',UserProfileView.as_view(),name='userprofile')
   

     #path('edit_profile/<int:pk>',EditMemberView.as_view(),name='edit')
    
]
