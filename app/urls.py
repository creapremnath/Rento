from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('home',home,name='home'),
     path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/',include('django.contrib.auth.urls')),
    
    # path('',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('register/',register,name='register'),
    path('property/',property,name='property'),
    path('rent/',rent,name='rent'),
    path('',login,name='login'),
    path('tenant/',tenant,name='tenant'),
    path('report/',report,name='report'),
    path('advance_tracker/',advance_tracker,name='advance_tracker'),
    path('settings/',settings,name='settings'),
    path('logout/',user_logout,name='logout'),
    path('sm/',samplemail,name='mailsend'),
    path('mbtn/',mailbtn,name='mbtn'),
    
]
