from django.contrib import admin
from django.urls import path, include
from .views import signupview, loginview, logoutview
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('signup/', signupview, name="SignUp"),
    path('login/', loginview, name="LogIn"),
    path('logout/', logoutview, name="LogOut"),
]

urlpatterns += staticfiles_urlpatterns()