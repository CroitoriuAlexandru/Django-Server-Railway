from django.urls import path
from .views import addEvent, dashboard


urlpatterns = [
    path('addEvent', addEvent, name="addEvent"),
    path('dashboard', dashboard, name="dashboard"),
]