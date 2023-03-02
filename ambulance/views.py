from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospital, Sub_counties, Ambulance
from django.utils import timezone
# Create your views here.
def all_ambulance(request):
    results = Ambulance.objects.all()
    return render(request,'home.html',{'ambulances':results})
