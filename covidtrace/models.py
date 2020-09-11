from django.db import models

# Create your models here.
from django.forms import ModelChoiceField


class Citymun (models.Model):
    cmdesc = models.CharField(max_length= 250, null= True)
    latitude = models.FloatField(max_length= 12, null= True)
    longitude = models.FloatField(max_length= 12, null= True)
    remarks = models.CharField(max_length= 500, null= True)
    CMCLASS = (

        ("City", "City"),
        ("Municipality", "Municipality")

    )
    cmclass = models.CharField(max_length=250, null= True, choices= CMCLASS)

    def __str__(self):
        return self.cmdesc

class Barangay (models.Model):
     bname = models.CharField(max_length= 250, null= True)
     latitude = models.FloatField(max_length= 12, null= True)
     longitude = models.FloatField(max_length= 12, null= True)
     estpop = models.IntegerField(null= True)
     blevel = models.IntegerField(null= True)
     remarks = models.CharField(max_length= 500, null= True)

     cities = models.cho
     def __str__(self):
         return self.bname

