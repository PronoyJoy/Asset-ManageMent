from rest_framework.serializers import ModelSerializer
from .models import Company,Device,Employee,DeviceLog

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'



class DeviceLogSerializer(ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__' 