from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, related_name="profile"
    )
    phone = PhoneNumberField()
    bio = models.TextField()
    
    def __str__(self):
        return str(self.user)
    
