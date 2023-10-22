from django.contrib import admin
from django.urls import path, include
from dotenv import load_dotenv

from .views import home
import os

load_dotenv()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('members.urls')),
]

if os.environ["DEBUG"] == "True":
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    
admin.site.site_header = "Login Portal"