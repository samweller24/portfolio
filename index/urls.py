from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.aboutus,name='about'),
    path('projects/', views.projects, name='project'),
    path('resume/', views.resume, name='resume'),

]