from django.shortcuts import render,HttpResponse
from .models import Property

# Create your views here.

def home(request):
    return render(request,'dashboard.html')

def property(request):
    properties = Property.objects.all()  # fetch all property records
    return render(request, 'property.html', {'properties': properties}) 

def rent(request):
    return render(request,'rent.html')


def report(request):
    return render(request,'report.html')

def settings(request):
    return render(request,'settings.html')


def tenant(request):
    properties = Property.objects.all()  # fetch all property records
    return render(request, 'tenant.html', {'properties': properties}) 


def advance_tracker(request):
    return render(request,'advance_tracker.html')


def logout(request):
    return HttpResponse("Logout Successfully")