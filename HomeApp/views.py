from django.shortcuts import render
from django.contrib.auth.models import User
from CoursesApp.models import Courses

# Create your views here.


def home(request):
    url = 'HOME'
    description = 'Welcome to Programming Site'

    courses = Courses.objects.all()
    users = User.objects.all()

    context = {'url': url, 'description': description, 'users': users, 'courses':courses}
    return render(request, 'HomeApp/home.html', context)
