from django.conf import settings
from django.shortcuts import render, redirect
from CalendarApp.forms import CalendarForm
from django.core.mail import send_mail  # SEND EMAIL'S
from django.contrib.auth.decorators import login_required  # LOGIN REQUIRED
from django.contrib import messages  # IMPORT MESSAGES

# Create your views here.

@login_required(login_url='login')
def calendar(request):

    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():

            messages.success(
                request, 'Gracias por tu interés, acabamos de recibir tu solucitud')

            name = request.POST['name']  # NAME
            subject = f'{name} quiere una cita contigo'

            phone = request.POST['phone']  # PHONE NUMBER
            date = request.POST['date']  # MESSAGE TEXT
            duration = request.POST['duration']  # DURATION
            email = request.POST['email']  # EMAIL

            # HTML CODE TO EMAIL
            text = f''' 
            <h3> Correo Electrónico : {email} </h3>\n
            <h3> Número de Teléfono : {phone} </h3>\n
            <h3> Data : {date} </h3>\n
            <h3> Duración de la Clase : {duration} Minutos</h3>\n
            '''

            email_from = settings.EMAIL_HOST_USER  # FROM EMAIL

            recipient_list = ['francesc.castell8@gmail.com']  # TO EMAILS

            send_mail(subject, message='', from_email=email_from,
                      recipient_list=recipient_list, html_message=text)

            return redirect('/')
    else:
        form = CalendarForm()

    url = 'CALENDARIO'
    description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, cumque.'

    context = {'url': url, 'description': description, 'form': form}
    return render(request, 'CalendarApp/calendar.html', context)
