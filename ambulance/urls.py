from django.urls import path
from . import views

app_name = 'ambulance'

urlpatterns = [
    path('',views.all_Subcounties, name='all_ambulance'),
    path('new_emergency/',views.request_ambulance, name='new_emergency')
]