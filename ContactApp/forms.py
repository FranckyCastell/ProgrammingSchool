from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}), required=True)

    phone = forms.IntegerField(label='Phone', widget=forms.NumberInput(
        attrs={'class': 'form-control'}), required=False)

    message = forms.CharField(label='Message', max_length=500, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'cols': 40}), required=True)
