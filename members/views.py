from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import User
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistrationForm
# from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "auth/registration.html"
    success_url = reverse_lazy("login")
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return render(request, "auth/registration.html")
    

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
            return render(request, "auth/login.html")
        
def logout_user(request):
    logout(request)
    return redirect("login")
    
