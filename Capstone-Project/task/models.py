from django.db import models
from django.contrib.auth.models import User


# Create your models here.
status_options = {'S': 'serviceable', 'U/S': 'unserviceable'}

class Equipment(models.Model):
    name = models.CharField(max_length=200, blank=False)
    part_no = models.CharField(max_length=200, blank=False)
    serial_no = models.CharField(max_length=50, unique=True, blank=False)
    svc_status = models.CharField(max_length=50, choices = status_options, blank=False)

    def __str__(self):
        return f"{self.name}"


class Technician(models.Model):
    rank = models.CharField(max_length=15)
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return f"{self.name}"
    