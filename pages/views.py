from django.shortcuts import render, redirect
from .models import Team
from cars.models import car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    team=Team.objects.all()
    featured_cars=car.objects.order_by('created_date').filter(is_featured=True)
    all_cars=car.objects.order_by('created_date')
    # search_fields=car.objects.values('model','city','year','body_style')
    model_search=car.objects.values_list('model',flat=True).distinct()
    city_search=car.objects.values_list('city',flat=True).distinct()
    year_search=car.objects.values_list('year',flat=True).distinct()
    body_style_search=car.objects.values_list('body_style',flat=True).distinct()
    data={
        'teams':team,
        'featured_cars':featured_cars,
        'all_cars': all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
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
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']
        email_subject='You have a new message from Car Zone Website regarding ' + subject
        message_body = 'Name: '+ name + '. Email:'+ email + 'Phone: '+phone + '.Message: '+ message
        admin_info = User.objects.filter(is_superuser=True)
        admin_email = []
        for i in admin_info:
            admin_email.append(i.email)
        send_mail(

                    email_subject,
                    message_body,
                    'singhprashant8759@gmail.com',
                    admin_email,
                    fail_silently=False,

                )
        messages.success(request,'Thank you for contacting us, we will get back to you soon!!')
        return redirect(contact)
    return render(request,'../templates/pages/contact.html')
