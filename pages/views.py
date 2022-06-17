from django.shortcuts import render
from .models import Team
from cars.models import car

# Create your views here.
def home(request):
    team=Team.objects.all()
    featured_cars=car.objects.order_by('created_date').filter(is_featured=True)
    all_cars=car.objects.order_by('created_date')
    data={
        'teams':team,
        'featured_cars':featured_cars,
        'all_cars': all_cars,
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
