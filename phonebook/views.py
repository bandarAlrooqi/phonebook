from django.shortcuts import render

from phonebook.models import *


# Create your views here.
def home(request):
    contacts = Phonebook.objects.select_related('number').all()
    return render(request, 'index.html', {'contacts': contacts})
