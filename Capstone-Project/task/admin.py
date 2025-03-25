from django.contrib import admin
from .models import Equipment, Maintenance, Technician

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_no', 'svc_status']
    list_filter = ['name']
    search_fields = ['name', 'part_no']

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ['rank', 'name']
    search_fields = ['name']

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'category', 'task_date']
    list_filter = ['equipment_name', 'category', 'task_date']
    search_fields = ['equipment_name', 'technician' 'category', 'task_date']