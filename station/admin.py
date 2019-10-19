from django.contrib import admin
from .models import Central, Drone, DroneLocation, CentralMeasurement

admin.site.register(Central)
admin.site.register(Drone)
admin.site.register(CentralMeasurement)
admin.site.register(DroneLocation)