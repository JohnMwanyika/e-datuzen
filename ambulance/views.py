from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospital, Sub_counties, Ambulance,Counties
from django.utils import timezone
from .forms import AmbulanceRequestForm
# Create your views here.
def all_ambulance(request):
    results = Ambulance.objects.all()
    return render(request,'home.html',{'ambulances':results})

def all_Subcounties(request):
    # scounties = Sub_counties.objects.all().select_related('hospitals')
    if request.method == 'POST':
        print('Posting data')
        emergency = AmbulanceRequestForm(request.POST)
        if emergency.is_valid():
            emergency.save()
            return redirect('ambulance:all_ambulance')
        else:
            form = AmbulanceRequestForm()
            hospitals = Hospital.objects.all()
            return render(request,'home.html',{'hospitals':hospitals,'form':form,'error_message':'Form not submited'})
        # if emergency.is_valid():
        #     print('form is valid')
        #     emergency.save()
        # return redirect('/ambulance')
    else:
        form = AmbulanceRequestForm()
        hospitals = Hospital.objects.all()
        return render(request,'home.html',{'hospitals':hospitals,'form':form})

# request ambulance
def request_ambulance(request):
    # form = AmbulanceRequestForm()
    if request.method == 'POST':
        print('Posting data')
        emergency = AmbulanceRequestForm(request.POST)
        if emergency.is_valid():
            print('form is valid')
            emergency.save()
            # return redirect('/ambulance')
    else:
        form = AmbulanceRequestForm()
    return redirect('ambulance:all_ambulance')