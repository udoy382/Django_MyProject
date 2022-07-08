from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about', views.about, name='Home'),
    path('contact', views.contact, name='Home'),
]