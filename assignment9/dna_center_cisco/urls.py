from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('auth/', views.auth_token, name='auth_token'),
    path('devices/', views.list_devices, name='list_devices'),
    path('interfaces/', views.device_interfaces, name='device_interfaces'),
]
