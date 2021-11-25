from django.conf import settings
from django.shortcuts import redirect, render
from ContactApp.forms import Contact
from django.core.mail import send_mail


# Create your views here.

def contact(request):

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form = Contact(request.POST)
            name = request.POST['name']
            subject = f'{name} Tiene una Duda'
            message = 'Correo Electronico de: ' + \
                request.POST['email'] + 'Su número de Teléfono es: ' + \
                request.POST['phone'] + ' Mensaje: ' + request.POST['message']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['francesc.castell8@gmail.com']
            send_mail(subject, message, email_from, recipient_list)

            return redirect('/')

    else:
        form = Contact()

    context = {'form': form}
    return render(request, 'ContactApp/contact.html', context)
