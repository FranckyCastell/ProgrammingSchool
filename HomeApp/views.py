from django.shortcuts import render
from HomeApp.models import Users
from CoursesApp.models import Categories

# Create your views here.


def home(request):
    url = 'HOME'
    description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, cumque.'

    categories = Categories.objects.all()
    users = Users.objects.all()

    context = {'url': url, 'description': description}
    return render(request, 'HomeApp/home.html', context)
