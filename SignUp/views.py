from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.password_validation import validate_password

# Create your views here.

def signupview(req):

    notsamepassword = False
    isSignup = True

    if req.method == 'POST':
        
        username = req.POST.get('username')
        password = req.POST.get('password')
        confirmpassword = req.POST.get('confirmpassword')

        if  password == confirmpassword and User.objects.filter(username=username).exists() == False and username != "Anonymous":

            password = make_password(password)
            user = User.objects.create(username = username, password = password)
            return redirect('/login')

        else:
            notsamepassword = True

    return render(req, '../templates/auth.html',{"name":"Sign Up", "isSignup": isSignup, "notsamepassword": notsamepassword})


def loginview(req):

    notfound = False
    user = None

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username = username, password = password)

        if user is not None:
            login(req, user=user)
            return redirect(f'{user}/')

        else:
            notfound = True

    isSignup = False
    
    return render(req, '../templates/auth.html',{"name":"Log In", "isSignup": isSignup, "notfound": notfound})


def logoutview(req):

    logout(req)
    return redirect('/login')

