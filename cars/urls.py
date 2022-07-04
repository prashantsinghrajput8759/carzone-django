
from django.urls import path
from . import views

urlpatterns = [
        path('',views.cars,name='cars'),
        path('<int:id>',views.cars_detail,name='cars_detail'),
        path('search',views.search,name='search'),
]
