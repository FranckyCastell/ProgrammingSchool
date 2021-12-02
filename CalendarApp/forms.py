from django import forms


class CalendarForm(forms.Form):

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'myname@email.com'}), required=True)

    phone = forms.IntegerField(label='Phone', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '123456789'}), required=True)

    date = forms.DateField(
        label='Date', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=True)

    duration = forms.CharField(label='Duration',
                               widget=forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': '30 min'}), required=True)
