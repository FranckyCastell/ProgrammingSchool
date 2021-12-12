from django.shortcuts import render

# Create your views here.


def home(request):
    url = 'HOME'
    description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, cumque.'

    context = {'url': url, 'description': description}
    return render(request, 'HomeApp/home.html', context)
