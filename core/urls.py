from django.urls import path
from .views import home, services, about, contact, careers
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('part-time-jobs/', views.part_time_jobs, name='part_time_jobs'),
    path('remote-jobs/', views.remote_jobs, name='remote_jobs'),
    path('apply/', views.apply, name='apply'),
    path('submit-application/', views.submit_application, name='submit_application'),
]