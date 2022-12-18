from django.shortcuts import render

from phonebook.models import *
from .form import *


# Create your views here.
def home(request):
    # query the database for all numbers and send only unique name to the template
    contacts = Phonebook.objects.all()
    return render(request, 'index.html', {'contacts': contacts})


def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        number = request.POST['number']
        Phonebook.objects.create(first_name=first_name, last_name=last_name,
                                 number=Number.objects.create(number=number))
    context = {
        'form': Contact(),
    }
    return render(request, 'add.html', context)


def display(request, pk):
    numbers = Number.objects.filter(phonebook=pk)
    phonebook = Phonebook.objects.get(id=pk)
    context = {
        'numbers': numbers,
        'phonebook': phonebook
    }
    return render(request, 'display.html', context)
