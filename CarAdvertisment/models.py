from django.db import models
from django.contrib.auth.models import User

# Create your models here.
status = [
    ('enabled', 'aktywny'),
    ('disabled', 'nieaktywny')
]

change_location = [
    ('ds', 'dolnośląskie'),
    ('kp', 'kujawsko_pomorskie'),
    ('lbl', 'lubelskie'),
    ('lub', 'lubuskie'),
    ('łód', 'łódzkie'),
    ('mlp', 'małopolskie'),
    ('maz', 'mazowieckie'),
    ('o', 'opolskie'),
    ('pkrp', 'podkarpackie'),
    ('pdls', 'podlaskie'),
    ('pom', 'pomorskie'),
    ('sl', 'slaśkie'),
    ('sw', 'świetokrzyskie'),
    ('wm', 'warmińsko_mazurskie'),
    ('wlkp', 'wielkopolskie'),
    ('zp', 'zachodniopomorskie')
]
# Create your models here.

class car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.brand} {self.model}'


class car_adveritsment(models.Model):

    # id = models.IntegerField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    year = models.IntegerField()  #metoda field.unique_for_year
    add_date = models.DateField()
    modified_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    status = models.CharField(choices=status, max_length=8)
    location = models.CharField(choices=change_location, max_length=4)
    telephone = models.IntegerField()
    description = models.TextField(max_length=1000)



class part_of_car_advertisment(models.Model):

    # id = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    add_date = models.DateField()
    modified_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    status = models.CharField(choices=status, max_length=8)
    location = models.CharField(choices=change_location, max_length=4)
    telephone = models.IntegerField()
    description = models.TextField(max_length=1000)

class service_advertisment(models.Model):

    service = [
        ('spraying', 'lakierowanie'),
        ('tinywork', 'blacharstwo'),
        ('car_mechanic', 'mechanika')
    ]

    # id = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(choices=service, max_length=12)
    add_date = models.DateField()
    modified_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=status, max_length=8)
    location = models.CharField(choices=change_location, max_length=4)
    telephone = models.IntegerField()
    description = models.TextField(max_length=1000)