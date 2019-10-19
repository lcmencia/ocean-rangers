from django.db import models


# Create your models here.
class Central(models.Model):
    name = models.CharField(max_length=65)
    lat = models.FloatField()
    lng = models.FloatField()


class Drone(models.Model):
    name = models.CharField(max_length=65)
    central = models.ForeignKey(Central, related_name='drone_central', on_delete=models.PROTECT)


class DroneLocation(models.Model):
    drone = models.ForeignKey(Drone, related_name='location_drone', on_delete=models.PROTECT)
    lat = models.FloatField()
    lng = models.FloatField()
    time = models.DateTimeField()

    def __unicode__(self):
        return "%s at %f,%f" % (self.drone, self.lat, self.lng)

    class Meta:
        ordering = ('-time', 'drone')


class CentralMeasurement(models.Model):
    central = models.ForeignKey(Central, related_name='measurement_central', on_delete=models.PROTECT)
    time = models.DateTimeField(blank=True, null=True)
    humedad = models.FloatField(blank=True, null=True)
    presion = models.FloatField(blank=True, null=True)
    presipitacion = models.FloatField(blank=True, null=True)
    direccion_viento = models.CharField(max_length=15, blank=True, null=True)
    velocidad = models.FloatField(blank=True, null=True)
    indice_uv = models.FloatField(blank=True, null=True)
    radiacion = models.FloatField(blank=True, null=True)