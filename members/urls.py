from django.urls import path
from .views import login_user, logout_user, UserRegisterView

urlpatterns = [
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path('registration', UserRegisterView.as_view(), name="registration"),
]
