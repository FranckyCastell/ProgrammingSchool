from django.shortcuts import render
from CoursesApp.models import Courses

# Create your views here.


def courses(request):

    url = 'COURSES'
    description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, cumque.'

    courses = Courses.objects.all()

    context = {'url': url, 'description': description, 'courses': courses}
    return render(request, 'Coursesapp/courses.html', context)
