from django.urls import path, include
from . import views

urlpatterns = [
   
    path('',views.contactus,name='contact'),
]