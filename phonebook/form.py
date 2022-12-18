from django import forms
from .models import *


class Contact(forms.ModelForm):
    # allow user to enter only 11 digits
    class Meta:
        model = Phonebook
        fields = ['first_name', 'last_name']

        # add list of numbers to the form


class Contact_number(forms.Form):
    number = forms.CharField(max_length=10, min_length=10)
