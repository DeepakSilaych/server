from django.db import models
from django.contrib.postgres.fields import ArrayField


class TrainStation(models.Model):
    station_name = models.CharField(max_length=100)
    station_code = models.CharField(max_length=10)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    neareststation = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    WarningLevel = models.IntegerField(default=0)
    rainfall = ArrayField(base_field=models.FloatField(), size=10)

    def __str__(self):
        return self.station_name


class AWSStation(models.Model):
    station_id = models.IntegerField()
    name = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    curr_rainfall = models.FloatField(default=0)
    curr_temp = models.FloatField(default=0)
    arr_rainfall = ArrayField(base_field=models.FloatField(), size=30)
    arr_temp = ArrayField(base_field=models.FloatField(), size=30)

    def __str__(self):
        return self.name
    
class StationData(models.Model):
    station = models.ForeignKey(AWSStation, on_delete=models.CASCADE)
    rainfall = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    windSpeed = models.FloatField(default=0)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.station.name + " " + str(self.timestamp)


class HourlyPrediction(models.Model):
    station = models.ForeignKey(AWSStation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pred_rainfall = ArrayField(base_field=models.FloatField(), size=25)

    def __str__(self):
        return self.station.name + " " + str(self.timestamp)

class DailyPrediction(models.Model):
    station = models.ForeignKey(AWSStation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pred_rainfall = ArrayField(base_field=models.FloatField(), size=5)

    def __str__(self):
        return self.station.name + " " + str(self.timestamp)
