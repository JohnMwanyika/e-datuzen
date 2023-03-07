from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospital, Sub_counties, Ambulance,Counties
from django.utils import timezone
# Create your views here.
def all_ambulance(request):
    results = Ambulance.objects.all()
    return render(request,'home.html',{'ambulances':results})

def all_Subcounties(request):
    # scounties = Sub_counties.objects.all().select_related('hospitals')

    hospitals = Hospital.objects.all()
    # related_hospitals  = Hospital.objects.filter(sub_county=hospitals.sub_county)

    # print(hospitals.ambulance_set.all)

    # return render(request,'home.html',{'hospitals':hospitals})
    return render(request,'home.html',{'hospitals':hospitals})