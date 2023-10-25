from django.contrib import admin
from django.urls import path, include
from dotenv import load_dotenv
from events import urls
from .views import home
import os

load_dotenv()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('members/', include('django.contrib.auth.urls')) ,
    path('members/', include('members.urls')),
    path('', include('events.urls')),
]

if os.environ["DEBUG"] == "True":
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    
# admin.site.site_header = "Login Portal"