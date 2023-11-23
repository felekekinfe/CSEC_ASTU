
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('CSEC_App.urls')),
    path('member/',include('members.urls')),
    path('member/',include('django.contrib.auth.urls'))
   
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

