from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ( CompanySerializer,
                          DeviceLogSerializer,DeviceSerializer,
                          EmployeeSerializer)
from .models import Company,Device,Employee,DeviceLog

# Create your views here.

class CompanyView(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class EmployeeView(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class DeviceView(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

class DeviceLogView(ModelViewSet):
    serializer_class = DeviceLogSerializer
    queryset = DeviceLog.objects.all()



