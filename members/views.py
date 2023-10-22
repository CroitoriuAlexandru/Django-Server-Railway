from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("home")
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Invalid credentials")
            return redirect("login")
    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return render(request, "authentificate/login.html")
        
def logout_user(request):
    logout(request)
    return redirect("login")
    