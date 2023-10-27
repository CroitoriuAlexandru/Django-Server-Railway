from django.urls import path
from .views import dashboard
from .views import clientsTables, createClient, updateClient, deleteClient


urlpatterns = [
    # path('', tables, name="tables"),
    path('clients', clientsTables, name="tableClients"),
    path('clients/create', createClient, name="createClient"),
    path('clients/update/<int:client_id>', updateClient, name="updateClient"),
    path('clients/delete/<int:client_id>', deleteClient, name="deleteClient"),
    path('dashboard', dashboard, name="dashboard"),
]