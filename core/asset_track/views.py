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
from rest_framework import permissions
# Create your views here.

# class IsCompanyAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         company = request.user.company
#         return company.admin == request.user

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
    authentication_classes = [TokenAuthentication]
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # Only show employees of the currently logged in user's company
            return Employee.objects.filter(company=user.company)
        else:
            # If user is not authenticated, return empty queryset
            return Employee.objects.none()
  

class DeviceView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Device.objects.all()

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # Only show employees of the currently logged in user's company
            return Device.objects.filter(company=user.company)
        else:
            # If user is not authenticated, return empty queryset
            return Device.objects.none()

class DeviceLogView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DeviceLogSerializer
    queryset = DeviceLog.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if user.is_authenticated and user.company:
            queryset = queryset.filter(employee__company=user.company)
        else:
            queryset = DeviceLog.objects.none()
        return queryset



