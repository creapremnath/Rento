from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'dashboard.html')


def property(request):
    return render(request,'property.html')

def rent(request):
    return render(request,'rent.html')


def report(request):
    return render(request,'report.html')

def settings(request):
    return render(request,'settings.html')


def tenant(request):
    return render(request,'tenant.html')


def advance_tracker(request):
    return render(request,'advance_tracker.html')


def logout(request):
    return HttpResponse("Logout Successfully")