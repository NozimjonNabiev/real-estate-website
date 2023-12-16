from django.db import models
from django.contrib.auth.models import AbstractUser

from .constants import USER_ROLES


class Address(models.Model):
    address_line_1 = models.CharField(max_length=255,)
    address_line_2 = models.CharField(blank=True, null=True)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=7, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    @staticmethod
    def create_from_geodata(longitute: float, latitute: float) -> "Address":
        pass
    

class Image(models.Model):
    image = models.ImageField(blank=True, null=True)


class Users(AbstractUser):
    role = models.CharField(max_length=255, choices=USER_ROLES.choices, default=USER_ROLES.CUSTOMER)
    email = models.CharField(unique=True, blank=True, null=True)
    password = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    role = models.CharField(blank=True, null=True)
    profile_image = models.ForeignKey(Image, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'