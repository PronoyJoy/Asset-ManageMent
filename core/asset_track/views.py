from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import ( CompanySerializer,
                          DeviceLogSerializer,DeviceSerializer,
                          EmployeeSerializer, 
                          RegisterSerializer, LoginSerializer)
from .models import Company,Device,Employee,DeviceLog
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication

from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors,

            },status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        
        return Response( {'status' : True,
                'message' : 'CREATED',},status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):  # sourcery skip: merge-nested-ifs
        data = request.data
        serializer= LoginSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors,

            },status.HTTP_400_BAD_REQUEST)
        
        user = authenticate( username = serializer.data['username'],
                             password = serializer.data['password'])
      
        if not user:
            return Response({
                    'status' : False,
                    'message' : "wrong credentials",

                },status.HTTP_400_BAD_REQUEST)
            
                

        token = Token()
        token.user = user
        token.save()

        return Response( {'status' : True,
                'message' : 'Logged In', 'token' : str(token) },status.HTTP_200_OK)

        

class CompanyView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    



