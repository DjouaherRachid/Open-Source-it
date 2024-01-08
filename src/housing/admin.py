from django.contrib import admin
from housing.models import Apartment, Reservation

# Register your models here.
admin.site.register(Apartment, admin.ModelAdmin)
admin.site.register(Reservation, admin.ModelAdmin)