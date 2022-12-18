from django import forms
from .models import *


class Contact(forms.ModelForm):
    # allow user to enter only 11 digits
    number = forms.CharField(max_length=11, min_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Phonebook
        fields = ['first_name', 'last_name', 'number']

        # add list of numbers to the form


class Contact_number(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['number']
