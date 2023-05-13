from rest_framework.serializers import ModelSerializer
from .models import Company,Device,Employee,DeviceLog
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):   # sourcery skip: merge-nested-ifs

        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('User already exists')
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('Email already exists')

        return data
    

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'],
                                    email= validated_data['email']
                                   )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()




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