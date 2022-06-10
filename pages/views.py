from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'../templates/pages/home.html')

def about(request):
    return render(request,'../templates/pages/about.html')

def services(request):
    return render(request,'../templates/pages/services.html')

def cars(request):
    return render(request,'../templates/pages/cars.html')

def contact(request):
    return render(request,'../templates/pages/contact.html')
