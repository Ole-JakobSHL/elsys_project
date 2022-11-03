## se https://innovasjon.ed.ntnu.no/ ctrl+f instanster, helt til apendixen) for å finne mer om dette.

from sqlite3 import Timestamp
from django.db import models

## må forandres for å legge inn de rette verdien for hlr -dukken 
class SensorData(models.Model):
    data = models.CharField(max_length=128)
    sensor_id = models.DateField()
    timestamp = models.DateField(auto_now_add=True)

    #def get_data(self):
    #    return merdata
        

    

    def __str__(self):
         return "data_verdiene: {}, sensorene: {} (enhet), tidspunktet: {}." .format(self.data, self.sensor_id, self.timestamp)




#        return f "Data_verdi: {self.data}, Sensorens_id: {self.sensor_id}, Tiden er: {self.timestamp}"
#        return f "Data_verdi" {self.data}, "Sensorens_id" {self.sensor_id}, "Tid" {self.timestamp},
#        ## to måterr å skrive denne call og return funksjonen.
#        return f"Name: {self.data}, Birthday: {self.date_of_birth}, height: {self.height} cm, has {self.nr_children} children."
#        return "Name: {}, Birthday: {}, height: {} cm, has {} children.".format(self.name, self.date_of_birth, self.height, self.nr_children)

## før man bruker klassen må man gjøre et par ting.
## i terminal:
# python manage.py makemigrations
# python manage.py migrate
## der etter må man åpne en python shell
# eks: python manage.py shell.
## der etter kan man fulle ut info;
## en måte å fulle ut dataen.
#p_1 = sensorData(data = "381763", sensor_id = "2022-10-27")
#p_1.save()
# print(p_1)
