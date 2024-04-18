from django.contrib import admin
from django.urls import path
from mynewapp.views import  *

urlpatterns = [
    path('',home_view),
    
]