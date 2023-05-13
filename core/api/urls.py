from django.urls import path,include
from rest_framework.authtoken import views

from asset_track.views import (
    CompanyView,EmployeeView,
    DeviceView,DeviceLogView,
    RegisterView,LoginView
    )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies',CompanyView,basename='companies')
router.register(r'employees',EmployeeView,basename='employees')
router.register(r'device',DeviceView,basename='device')
router.register(r'device_logs',DeviceLogView,basename='device_logs')


urlpatterns = [

    path('',include(router.urls)),
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view())
    # path('api-token-auth/', views.obtain_auth_token,name='create-token'),
    

]
