from django.db import models

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
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(15)
    model = models.CharField(15)


class car_adveritsment(models.Model):

    id = models.IntegerField(primary_key=True)
    id_car = models.ForeignKey('car', on_delete=models.CASCADE)
    id_user = models.IntegerField()
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    year = models.IntegerField() #metoda field.unique_for_year
    add_date = models.DateField()
    modified_date = models.DateField()
    end_date = models.DateField()
    prize = models.IntegerField()
    status = models.CharField(choices=status)
    location = models.CharField(choices=change_location)
    telephone = models.IntegerField(max_length=9)
    description = models.TextField(1000)



class part_of_car_advertisment(models.Model):

    id = models.IntegerField(primary_key=True)
    id_user = models.IntegerField()
    name = models.CharField(max_length=50)
    add_date = models.DateField()
    modified_date = models.DateField()
    end_date = models.DateField()
    prize = models.IntegerField()
    status = models.CharField(choices=status)
    location = models.CharField(choices=change_location)
    telephone = models.IntegerField(max_length=9)
    description = models.TextField(1000)

class service_avertisment(models.Model):

    service = [
        ('spraying', 'lakierowanie'),
        ('tinywork', 'blacharstwo'),
        ('car_mechanic', 'mechanika')
    ]

    id = models.IntegerField(primary_key=True)
    id_user = models.IntegerField()
    service = models.CharField(choices=service)
    add_date = models.DateField()
    modified_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=status)
    location = models.CharField(choices=change_location)
    telephone = models.IntegerField(max_length=9)
    description = models.TextField(1000)
