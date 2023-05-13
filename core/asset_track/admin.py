from django.contrib import admin
from .models import Company,Device,Employee,DeviceLog
# Register your models here.
admin.site.register(Company)
admin.site.register(Device)
admin.site.register(DeviceLog)
admin.site.register(Employee)