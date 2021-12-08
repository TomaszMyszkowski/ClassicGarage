from django.db import models
from django.contrib.auth.models import User

# Create your models here.
status = [
    ('aktywne', 'aktywne'),
    ('nieaktywne', 'nieaktywne')
]

change_location = [
    ('dolnośląskie', 'dolnośląskie'),
    ('kujawsko_pomorskie', 'kujawsko_pomorskie'),
    ('lubelskie', 'lubelskie'),
    ('lubelskie', 'lubelskie'),
    ('łódzkie', 'łódzkie'),
    ('małopolskie', 'małopolskie'),
    ('mazowieckie', 'mazowieckie'),
    ('opolskie', 'opolskie'),
    ('podkarpackie', 'podkarpackie'),
    ('podlaskie', 'podlaskie'),
    ('pomorskie', 'pomorskie'),
    ('śląskie', 'śląskie'),
    ('świetokrzyskie', 'świetokrzyskie'),
    ('warmińsko_mazurskie', 'warmińsko_mazurskie'),
    ('wielkopolskie', 'wielkopolskie'),
    ('zachodniopomorskie', 'zachodniopomorskie')
]
# Create your models here.

class car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.brand} {self.model}'


class CarAdveritsment(models.Model):

    # id = models.IntegerField(primary_key=True)
    # id_car = models.ForeignKey('car', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField()  #metoda field.unique_for_year
    # add_date = models.DateField()
    # modified_date = models.DateField()
    # end_date = models.DateField()
    price = models.IntegerField()
    status = models.CharField(choices=status, max_length=10)
    location = models.CharField(choices=change_location, max_length=19)
    telephone = models.IntegerField()
    description = models.TextField(max_length=1000)



class PartOfCarAdvertisment(models.Model):

    # id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # name = models.CharField(max_length=50)
    # add_date = models.DateField()
    # modified_date = models.DateField()
    # end_date = models.DateField()
    price = models.IntegerField()
    status = models.CharField(choices=status, max_length=10)
    location = models.CharField(choices=change_location, max_length=19)
    telephone = models.IntegerField()
    description = models.TextField(max_length=1000)

class ServiceAdvertisment(models.Model):

    service = [
        ('lakierowanie', 'lakierowanie'),
        ('blacharstwo', 'blacharstwo'),
        ('mechanika', 'mechanika')
    ]

    # id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    service = models.CharField(choices=service, max_length=12)
    # add_date = models.DateField()
    # modified_date = models.DateField()
    # end_date = models.DateField()
    status = models.CharField(choices=status, max_length=10)
    location = models.CharField(choices=change_location, max_length=19)
    telephone = models.IntegerField()
    description = models.TextField(max_length=1000)