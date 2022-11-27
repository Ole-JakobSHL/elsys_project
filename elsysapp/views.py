from django.shortcuts import render
from django.http import HttpResponse, QueryDict, JsonResponse
from django.middleware import csrf

from .models import SensorData
from django.shortcuts import render
from django.db import models 


def index(request):
   print("Dette blir printa i terminalen")
   context = {}
   all_sensor_data = SensorData.objects.all() #Henter ut all sensordata fra databasen. 
   context['all_sensor_data'] = all_sensor_data #Legger sensordata til som en variabel som kan brukes i Template. 
   return render(request, "elsysapp/index.html", context)


def get_sensor_data(request):
    if request.method == "POST": 
        data =  QueryDict(request.body) # Gjør data fra request om til en dictionary
        sensor_id = data['sensorID'] # Lagrer sensor_id til requesten 
        sensor_value = data['sensorData'] # Lagrer sensorverdien til requesten
    
        p_1 = SensorData(data = sensor_value, sensor_id = sensor_id)
        p_1.save()

        #from elsysapp.models import SensorData
        #   Sensor_1 = SensorData()
        # Skriv koden for å lage og lagre et sensorobjekt her. 
        
        return HttpResponse("")


    ## må være her pga sikkerhet
    elif request.method == "GET":
        """Dette MÅ være med! Sikkerhetsgreier."""
        csrf.get_token(request)
        return HttpResponse("")







        #def index(request):
#    print("fuck you big boy why are you stealing my dogs?")
#    context = {} # Tom dictionary som blir brukt senere!
#    return render(request, "elsysapp/index.html", context)
