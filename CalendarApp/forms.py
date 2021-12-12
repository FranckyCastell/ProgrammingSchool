from django import forms


class CalendarForm(forms.Form):

    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Marc Picó Mascaro'}), required=True)

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'myname@email.com'}), required=True)

    phone = forms.IntegerField(label='Phone', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '123456789'}), required=True)

    message = forms.CharField(label='Mensaje', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}), required=True)
