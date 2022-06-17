from django.shortcuts import render

# Create your views here.

def cars(request):
    return render(request,'../templates/cars/cars.html')
