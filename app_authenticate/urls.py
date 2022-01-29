from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="auth-login"),
    path('logout', views.logoff, name="auth-logout"),
    path('register', views.register, name="auth-register"),
]