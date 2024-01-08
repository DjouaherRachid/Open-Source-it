from django.db import models
from users.models import User

# Create your models here.
class Apartment(models.Model):
    owner = models.ForeignKey(User, related_name='apartments', on_delete=models.CASCADE)
    area = models.PositiveIntegerField()
    max_capacity = models.PositiveIntegerField()
    address = models.CharField(max_length=512)
    price_per_night = models.FloatField()
    is_available = models.BooleanField(default=False)


class Reservation(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='reservations', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.FloatField()