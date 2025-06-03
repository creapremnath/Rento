from django.urls import path
from .views import *


urlpatterns=[
    path('',home,name='home'),
    path('property/',property,name='property'),
    path('rent/',rent,name='rent'),
    path('tenant/',tenant,name='tenant'),
    path('report/',report,name='report'),
    path('advance_tracker/',advance_tracker,name='advance_tracker'),
    path('settings/',settings,name='settings'),
    path('logout/',logout,name='logout'),
]