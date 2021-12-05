from django import forms


class CalendarForm(forms.Form):

    name = forms.CharField (label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Marc Picó Mascaro'}), required=True)

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'myname@email.com'}), required=True)

    phone = forms.IntegerField(label='Phone', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '123456789'}), required=True)

    date = forms.DateField(
        label='Date', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=True)

    time = forms.CharField(label='Time',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10:00h - 11:00h'}), required=True)

    