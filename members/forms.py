from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    # error_css_class = '!bg-red-400'
    input_style = "block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={
            "class": input_style,
            "placeholder": "Email",
            },
        ))
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.EmailInput(attrs={
            "class": input_style,
            "placeholder": "First Name"
            }),
        
        
    )

    last_name = forms.CharField(
        max_length=150, 
        required=True,  
        widget=forms.EmailInput(attrs={
            "class": input_style,
            "placeholder": "Last Name"
        }),        
    )
    
    
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs['placeholder'] = "Username"
        
        self.fields["username"].widget.attrs['class'] = self.input_style
        self.fields["password1"].widget.attrs['class'] = self.input_style
        self.fields["password2"].widget.attrs['class'] = self.input_style
        # for fieldname in ["username", "password1", "password2"]:
        # self.fields[fieldname].help_text = None
            
    
    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     user.first_name = self.cleaned_data["first_name"]
    #     user.last_name = self.cleaned_data["last_name"]
        
    #     if commit:
    #         user.save()
    #     return user