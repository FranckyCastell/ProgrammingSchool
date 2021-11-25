from django.shortcuts import render
from django.contrib.auth.models import User
from CoursesApp.models import Categories

# Create your views here.


def home(request):
    url = 'HOME'
    description = 'Welcome to Programming Site'

    categories = Categories.objects.all()
    users = User.objects.all()

    context = {'url': url, 'description': description, 'users': users, 'categories':categories}
    return render(request, 'HomeApp/home.html', context)
