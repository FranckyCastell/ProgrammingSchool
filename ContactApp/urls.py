from django.urls import path
from ContactApp import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
]
