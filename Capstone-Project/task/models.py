from django.db import models
from django.contrib.auth.models import User


# Create your models here.
status_options = {'serviceable':'S', 'unserviceable':'U/S'}

class Equipment(models.Model):
    name = models.CharField(max_length=200, blank=False)
    part_no = models.CharField(max_length=200, blank=False)
    serial_no = models.CharField(max_length=50, unique=True, blank=False)
    svc_status = models.CharField(max_length=50, choices = status_options, blank=False)
    remark = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"


class Technician(models.Model):
    rank = models.CharField(max_length=15)
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=False, max_length=100)
    profile_picture = models.ImageField()

    def __str__(self):
        return f"{self.name}"
    
maint_category = {
    'periodic': 'Periodic',
    'preventive': 'Preventive',
    'category A': 'Category A',
    'category B': 'Category B',
    'category C': 'Category C',
    'category D': 'Category D'
}
class Maintenance(models.Model):
    equipment_name = models.ForeignKey(Equipment, on_delete=models.PROTECT, related_name='task_record')
    equipment_serial_no = models.ForeignKey(Equipment, on_delete=models.PROTECT)
    technician = models.ForeignKey(Technician, on_delete=models.PROTECT, related_name='task_record')
    category = models.CharField(max_length=50, choices=maint_category, blank=False)
    task_description = models.CharField(max_length=255, blank=False)
    task_date = models.DateField(auto_now_add=True, blank=False)
    remarks = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.category} maintenance on {self.equipment_name}, on {self.task_date}."
