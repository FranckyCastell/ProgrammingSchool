from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import html
from ContactApp.forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages  # IMPORT MESSAGES

# Create your views here.


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            messages.success(request, 'Gracias por tu mensaje, intentaremos contactar contigo lo antes Posible.')

            name = request.POST['name']  # NAME
            subject = f'{name} tiene una duda'

            phone = request.POST['phone']  # PHONE NUMBER
            mensaje = request.POST['message']  # MESSAGE TEXT
            email = request.POST['email']  # EMAIL

            # HTML CODE TO EMAIL
            text = f''' 
            <h3> Correo Electrónico : {email} </h3>\n
            <h3> Número de Teléfono : {phone} </h3>\n
            <h3> Mensaje : {mensaje} </h3>\n
            '''

            email_from = settings.EMAIL_HOST_USER  # FROM EMAIL

            recipient_list = ['francesc.castell8@gmail.com']  # TO EMAILS

            send_mail(subject, message='', from_email=email_from,
                      recipient_list=recipient_list, html_message=text)

            return redirect('contact')
    else:
        form = ContactForm()

    url = 'CONTACTO'
    description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, cumque.'

    context = {'form': form, 'url': url, 'description': description}
    return render(request, 'ContactApp/contact.html', context)
