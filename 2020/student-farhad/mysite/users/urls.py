from django.urls import path
from .views import register, user_login, home

app_name = 'users'

urlpatterns = [
    path('register/', register),
    path('login', user_login, name='user_login'),
    path('', home, name='home')
]