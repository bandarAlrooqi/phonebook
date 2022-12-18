from django import forms
from .models import *


class Contact(forms.ModelForm):
    class Meta:
        model = Phonebook
        fields = ['first_name', 'last_name']
        # make all fields required
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
        }


class Contact_number(forms.Form):
    number = forms.CharField(max_length=10, min_length=10, required=True)
