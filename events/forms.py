from django import forms
from .models import Client, Event, Service, GenericService
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
class ClientForm(forms.ModelForm):

    name = forms.CharField(
        label='', 
        max_length=200, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-1.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                }
            )
        )

    phone = PhoneNumberField(
        label='', 
        widget=PhoneNumberPrefixWidget(
            country_choices=[
                 ("+40", "Ro +40"),
                 ("FR", "France"),
            ],
            attrs={
                'placeholder': 'Phone',
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-1.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                }
            )
        )

    class Meta:
        model = Client
        fields = '__all__'
            

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