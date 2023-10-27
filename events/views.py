from django.shortcuts import render
from django.shortcuts import redirect, resolve_url
from django.urls import reverse
from .forms import ClientForm
from .models import Client, Event, Service, GenericService

# Create your views here.
def clientsTables(request):
    clients = Client.objects.all()
    context = {'clients': clients, 'form': ClientForm()}
    return render(request, 'tables.html', context)


def createClient(request):
    if request.method == "POST":  
        form = ClientForm(request.POST)  
        if form.is_valid():
            print(form.data.get('phone'))
            form.save()
            return redirect(reverse('tableClients'))
        
        context = {'form': form, 'btnText': 'Create'}
        return render(request, 'forms/client.html', context)

    context = {'form': ClientForm(), 'btnText': 'Create'}
    return render(request,'forms/client.html', context)

def updateClient(request, client_id): 
    client = Client.objects.get(id=client_id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance = client)
        if form.is_valid():  
            try:  
                form.save()
                print("redirect")
                return redirect('tables')  
            except:
                print("error")
                pass
    else:
        context = {}

        context['form'] = ClientForm(instance = client)
        context['btnText'] = "Update"
        return render(request,'forms/client.html', context)

def deleteClient(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('/tables')


def dashboard(request):
    return render(request, 'dashboard.html')