from django.contrib import admin
from django.urls import path
from .views import index #Relativ import av viewsfunksjonen

appname = "elsysapp"
urlpatterns = [
    path('', index, name='index'),
]

