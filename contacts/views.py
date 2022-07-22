
from django.shortcuts import render,redirect

from contacts.models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def inquiry(request):
    if request.method=='POST':
        car_id=request.POST['car_id']
        car_title=request.POST['car_title']
        user_id=request.POST['user_id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        customer_need=request.POST['customer_need']
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']


        if request.user.is_authenticated:
            has_enquired=Contact.objects.all().filter(car_id=car_id,user_id=user_id)

            if(has_enquired):
                messages.error(request,'you have already enquired for this car, plz wait until we get back to u')
                return redirect('/cars/'+car_id)
            else:
                contact=Contact(car_id=car_id,car_title=car_title,user_id=user_id,
                first_name=first_name,last_name=last_name,customer_need=customer_need,city=city,
                state=state,email=email,phone=phone,message=message)

                admin_info = User.objects.filter(is_superuser=True)
                admin_email = []
                for i in admin_info:
                    admin_email.append(i.email)
                send_mail(

                    'New Car Enquiry',
                    'You have a new enquiry for the car '
                    + car_title + 'plz check your admin pannel for more info',
                    'singhprashant8759@gmail.com',
                    admin_email,
                    fail_silently=False,

                )
                contact.save()

                messages.success(request,'Your request has been submitted, we will get back to you shortly.')
                return redirect('/cars/'+car_id)

        
    return redirect('/cars/'+car_id)

