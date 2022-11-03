from django.contrib import admin
from django.urls import path
from .views import index #Relativ import av viewsfunksjonen

appname = "nettside_hlrdukke"
urlpatterns = [
    path('', index, name='index'),
]

    