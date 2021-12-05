from django.urls import path
from AboutApp import views

urlpatterns = [
    path('about', views.about, name='about'),
]
