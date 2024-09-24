from django.db import models
from musician.models import musician_model
from datetime import datetime
# Create your models here.

class album_model(models.Model):
    Album_Name = models.CharField(max_length=75)
    Musician = models.ForeignKey(musician_model,on_delete=models.CASCADE)
    Album_Release_Date = models.DateTimeField(default=datetime.now())
    Choice = [
        (1, '1 - Very Bad'),
        (2, '2 - Bad'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    Rating = models.IntegerField(choices=Choice)

    def __str__(self) -> str:
        return self.Album_Name
