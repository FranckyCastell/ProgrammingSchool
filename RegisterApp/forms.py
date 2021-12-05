from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm (UserCreationForm):
    username = forms.CharField(label='Usuario', required=True)
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput, required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k: "" for k in fields}
