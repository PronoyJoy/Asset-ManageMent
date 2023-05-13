from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Companies'
    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    available = models.BooleanField()

    def __str__(self):
        return f"{self.name} ({self.available})"

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assigned = models.DateTimeField()
    returned = models.DateTimeField(null=True, blank=True)
    condition = models.TextField()

    def __str__(self):
        return f"{self.device.name} ({self.employee.name}) "
    
    class Meta:
        get_latest_by = ['assigned']
