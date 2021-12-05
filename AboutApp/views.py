from django.shortcuts import render
from HomeApp.models import Users

# Create your views here.


def about(request):

    users = Users.objects.all()

    url = 'SOBRE NOSOTROS'
    description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, cumque.'

    context = {'url': url, 'description': description, 'users': users}

    return render(request, 'AboutApp/about.html', context)
