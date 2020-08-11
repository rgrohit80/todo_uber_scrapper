from django.db import models


# Create your models here.
class Cab(models.Model):
    driver = models.CharField(max_length=100, default=" ")
    trip_name = models.CharField(max_length=150, default=" ")
    x_loc = models.FloatField(null=True, blank=False, default=0)
    y_loc = models.FloatField(null=True, blank=False, default=0)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.driver


class Rider(models.Model):
    rider_name = models.CharField(max_length=100, default="User")

    def __str__(self):
        return self.rider_name


class Location(models.Model):
    loc_x = models.FloatField(null=True, blank=False, default=0)
    loc_y = models.FloatField(null=True, blank=False, default=0)

    def __str__(self):
        return "({},{})".format(self.loc_x, self.loc_y)


class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='trips')
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    stat = [
        ('IP', 'In Progress'),
        ('CP', 'Completed')
    ]
    status = models.CharField(max_length=50, choices=stat)
    price = models.FloatField()
    src_loc = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='trip_src')
    dest_loc = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='trip_dest')

    def __str__(self):
        return self.trip_id
