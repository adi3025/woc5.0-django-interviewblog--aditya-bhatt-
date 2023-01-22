from django.urls import path,include
from django.contrib import admin
from . import views 

urlpatterns = [
    path('',views.admin),
    path('PostLogin',views.PostLogin),
    path('login/',include('login.urls')),
    path ('login/',include('django.contrib.auth.urls')),
    path('register/',views.register),
    
]