from django import forms


class Contact (forms.Form):
    name = forms.CharField(label='Name', max_length=50, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    phone = forms.IntegerField(label='Phone', max_value=10 ,required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    message = forms.CharField(label='Mensaje', widget=forms.Textarea(
        attrs={'rows': 6, 'cols': 40, 'class':'form-control'}), required=True)
