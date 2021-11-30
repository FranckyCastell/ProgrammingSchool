from django.urls import path
from CalendarApp import views

urlpatterns = [
    path('calendar', views.calendar, name='calendar'),
]
