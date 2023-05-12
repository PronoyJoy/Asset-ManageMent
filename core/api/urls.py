from django.urls import path,include

from asset_track.views import (
    CompanyView,EmployeeView,
    DeviceView,DeviceLogView
    )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies',CompanyView,basename='companies')
router.register(r'employees',EmployeeView,basename='employees')
router.register(r'device',DeviceView,basename='device')
router.register(r'device_logs',DeviceLogView,basename='device_logs')


urlpatterns = [

    path('',include(router.urls)),

]
