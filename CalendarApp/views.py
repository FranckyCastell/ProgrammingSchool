from django.shortcuts import render
from CalendarApp.forms import CalendarForm

# Create your views here.


def calendar(request):

    form = CalendarForm()
    url = 'CALENDARIO'
    description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, cumque.'

    context = {'url': url, 'description': description, 'form': form}
    return render(request, 'CalendarApp/calendar.html', context)
