from django.urls import path
from .views import vendor_create, vendor_list

app_name = 'vendor'

urlpatterns = [
    path('', vendor_create, name='vendor'),
    path('list/', vendor_list, name='vendor_list'),
]