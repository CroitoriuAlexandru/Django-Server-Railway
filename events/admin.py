from django.contrib import admin
from .models import Client, Event, Service, GenericService

# Register your models here.
admin.site.register(Client)
admin.site.register(Event)
admin.site.register(Service)
admin.site.register(GenericService)

