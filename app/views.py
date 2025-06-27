from django.shortcuts import render,HttpResponse,redirect
from .models import Property
from django.core.mail import send_mail
from django.conf import settings
from background_task import background
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages



from django.contrib.auth import get_user_model

User = get_user_model()


def register(request):

    if user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        if not email:
            messages.error(request, "Email is required.")
            return render(request, 'register.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'register.html')

        #  Create user with correct fields
        user = User.objects.create_user(
            email=email,
            password=password,
            name=full_name,
            mobile=mobile,
            address=address
        )

        user.save()

        messages.success(request, "User registered successfully!")
        return redirect('login')

    return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)  

        if user is not None:
            auth_login(request, user)
            return redirect('home')   
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')

@login_required(login_url='login')
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


def user_logout(request):
    auth_logout(request)
    messages.info(request,'Logged out Successfully!')
    return redirect('login')






def samplemail(request):
    subject = "This is a Sample Subject Mail"
    message = "Hello How are you My Boy"
    from_email = "creativepremnath@gmail.com" # This will now correctly access your setting
    recipient_list = ['premnathskills@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Mail sent successfully.")


def mailbtn(request): # Assuming mailbtn is a view for a button
    # You might render a template here or redirect
    return render(request,"mail.html") # Placeholder response

@background(schedule=60)
def send_email(request):
    return samplemail(request)
