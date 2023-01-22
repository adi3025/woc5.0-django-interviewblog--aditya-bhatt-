
from django.urls import path
from . import views



urlpatterns = [
    path('loginu',views.login_user,name = "login"),
    
]