from django import forms
from .models import Client, Event, Service, GenericService

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name', 'phone']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['client', 'address', 'date', 'duration']
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['provider_user', 'generic_service', 'event']

class GenericServiceForm(forms.ModelForm):
    class Meta:
        model = GenericService
        fields = ['title', 'description']