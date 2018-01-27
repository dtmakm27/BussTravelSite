from django.db import models

# Create your models here. Trips are all the routes we're using


class Trips(models.Model):
    time_Of_Departure = models.DateTimeField(default='2000-09-04 06:00')
    time_Of_Arrival = models.DateTimeField(default='2000-09-04 06:00')
    city_Of_Departure = models.CharField(max_length=250, default='')
    city_Of_Arrival = models.CharField(max_length=250, default='')
    duration_Of_Trip = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    fees = models.DecimalField(max_digits=6, decimal_places=2, default=0)


class Change(models.Model):
    route = models.ForeignKey(Trips, on_delete=models.CASCADE, default='')
    time_Of_Departure = models.DateTimeField(default='2000-09-04 06:00')
    time_Of_Arrival = models.DateTimeField(default='2000-09-04 06:00')
    city_Of_Departure = models.CharField(max_length=250, default='')
    city_Of_Arrival = models.CharField(max_length=250, default='')
    duration_Of_Trip = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    fees = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    # def __init__(self, departure, arival, citya, cityb, duration, fees):
    #     self.time_Of_Departure = departure
    #     self.time_Of_Arrival = arival
    #     self.city_Of_Departure = citya
    #     self.city_Of_Arrival = cityb
    #     self.duration_Of_Trip = duration
    #     self.fees = fees

    def __str__(self):
       return self.city_Of_Departure + ' ' + self.city_Of_Arrival