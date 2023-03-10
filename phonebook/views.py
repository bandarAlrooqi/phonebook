from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import formset_factory
from .form import *
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    contacts = Phonebook.objects.all()
    return render(request, 'index.html', {'contacts': contacts})


def add(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            user = form.save()
            # get all numbers from the form
            numbers = request.POST.dict()
            # remove the csrf token and the name from the dictionary
            numbers.pop('csrfmiddlewaretoken')
            numbers.pop('first_name')
            numbers.pop('last_name')
            # loop through the dictionary and save the numbers
            for number in numbers.values():
                Number.objects.create(number=number, phonebook=user)
            return HttpResponseRedirect('/display/' + str(user.id))
    return render(request, 'add.html', {'form': Contact(), 'formset': formset_factory(Contact_number)})


def display(request, pk):
    # get or 404 returns a 404 error if the object is not found
    contact = get_object_or_404(Phonebook, pk=pk)
    numbers = Number.objects.filter(phonebook=pk)
    context = {
        'numbers': numbers,
        'phonebook': contact
    }
    return render(request, 'display.html', context)
