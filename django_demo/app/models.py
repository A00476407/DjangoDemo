from django.db import models

# Create your models here.

class Rooms(models.Model):
    id = models.AutoField(primary_key = True)
    price = models.IntegerField(null = False, default = 0)
    type_id = models.IntegerField(null = False, default = 0)

class RoomTypes(models.Model):
    type_id = models.AutoField(primary_key = True)
    type_name = models.CharField(max_length = 200)
    bed_type = models.CharField(max_length = 200)
    occupancy = models.IntegerField(null = False, default = 0)
    size = models.CharField(max_length = 200)
    view = models.CharField(max_length = 200)