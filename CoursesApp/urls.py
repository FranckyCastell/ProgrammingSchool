from django.urls import path
from CoursesApp import views

urlpatterns = [
    path('courses', views.courses, name='courses')
]
