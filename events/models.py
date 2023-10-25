from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    
    def __str__(self):
        return self.phone + " | " + self.name

    
class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default='')
    date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    duration = models.DurationField(null=True, blank=True)
    
    def __str__(self):
        return str(self.date.strftime("%Y-%m-%d %H:%M")) + " | Client: " + self.client.name + " | Address: " + self.address
    
class GenericService(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Service(models.Model):
    provider_user = models.ForeignKey(User, on_delete=models.CASCADE)
    generic_service = models.OneToOneField(GenericService, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
