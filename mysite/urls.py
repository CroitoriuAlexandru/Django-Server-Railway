from django.contrib import admin
from django.urls import path, include
from .views import home
from dotenv import load_dotenv
import os

load_dotenv()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
]

if os.environ["DEBUG"] == "True":
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    
