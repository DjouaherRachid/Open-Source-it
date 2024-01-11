from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

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

# Signal to create the group and add the user to it when a new user is saved
@receiver(post_save, sender=User)
def create_user_group(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name=instance.role)
        instance.groups.add(group)