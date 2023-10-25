from django.shortcuts import render
from .forms import ClientForm
from .models import Client, Event, Service, GenericService

# Create your views here.
def addEvent(request):
    return render(request, 'addEvent.html')

def dashboard(request):
    return render(request, 'dashboard.html')