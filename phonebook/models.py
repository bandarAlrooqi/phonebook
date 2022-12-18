from django.db import models


# Create your models here.


# create a model for the phonebook
class Phonebook(models.Model):
    # store name
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Number(models.Model):
    # store phone number
    number = models.CharField(max_length=255)
    phonebook = models.ForeignKey(Phonebook, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
