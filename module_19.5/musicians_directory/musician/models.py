from django.db import models

# Create your models here.

class musician_model(models.Model):
    First_Name = models.CharField(max_length=75)
    Last_Name = models.CharField(max_length=75)
    Email = models.EmailField()
    Phone_Number = models.IntegerField()
    Instrument_Type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.First_Name
