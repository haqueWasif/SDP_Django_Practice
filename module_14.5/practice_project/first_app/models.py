from django.db import models

# Create your models here.

class practice_model(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    integer_field = models.IntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()

    def __str__(self) -> str:
        return f"Name : {self.name}"