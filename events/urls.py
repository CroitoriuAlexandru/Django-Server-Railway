from django.urls import path
from .views import tables, dashboard
from .views import createClient, updateClient, deleteClient


urlpatterns = [
    path('tables', tables, name="tables"),
    path('tables/clients/create', createClient, name="createClient"),
    path('tables/clients/update/<int:client_id>', updateClient, name="updateClient"),
    path('tables/clients/delete/<int:client_id>', deleteClient, name="deleteClient"),
    path('dashboard', dashboard, name="dashboard"),
]