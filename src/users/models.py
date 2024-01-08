from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

'''
    Base user
'''
class User(AbstractUser):
    # Base user model

    # will automatically add a timestamp as soon as the record is created and do not gets updated on updating the record
    created_at = models.DateTimeField(auto_now_add=True)

    ADMINISTRATOR = 'admin'
    OWNER = 'owner'
    CUSTOMER = 'customer'

    ROLES = (
        (ADMINISTRATOR, "Administrator"),
        (OWNER, "Owner"),
        (CUSTOMER, "Customer")
    )
    
    role = models.CharField(max_length=32, choices=ROLES, default='customer')

    def __str__(self):
        return self.username