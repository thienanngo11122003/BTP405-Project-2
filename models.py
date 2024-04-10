from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    party_size = models.IntegerField()
