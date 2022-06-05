from django.db import models

# Create your models here.
class User(models.Model):
    Aadhaar_Number = models.BigIntegerField()
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20)
    Mobile_Number = models.BigIntegerField()
    Dose = models.IntegerField()
    Vaccine_Name = models.CharField(max_length=20)