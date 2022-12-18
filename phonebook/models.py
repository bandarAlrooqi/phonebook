from django.db import models


# Create your models here.
class Number(models.Model):
    # store phone number
    number = models.CharField(max_length=255)

    def __str__(self):
        return str(self.number)


# create a model for the phonebook
class Phonebook(models.Model):
    # store name
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # store phone number
    number = models.ForeignKey(Number, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
