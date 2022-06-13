from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    team=Team.objects.all()
   
    data={
        'teams':team,
    }
    return render(request,'../templates/pages/home.html',data)

def about(request):
    team=Team.objects.all()
    
    data={
        'teams':team,
    }
    return render(request,'../templates/pages/about.html',data)

def services(request):
    return render(request,'../templates/pages/services.html')

def cars(request):
    return render(request,'../templates/pages/cars.html')

def contact(request):
    return render(request,'../templates/pages/contact.html')
