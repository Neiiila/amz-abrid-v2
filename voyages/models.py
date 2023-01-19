import datetime
from django.db import models

# Create your models here.

class Voyage(models.Model) : 
    id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=200)
    depart = models.CharField(max_length=200)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.destination

class Transport(models.Model) :
    ice = models.IntegerField(max_length=15, primary_key=True)
    societe = models.CharField(max_length=100)
    tel = models.IntegerField(max_length=10)
    email = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default="Avion")

class Hotel(models.Model ) : 
    ice = models.IntegerField(max_length=15, primary_key=True)
    nom = models.CharField(max_length=100)
    classification = models.CharField(max_length=100 , default ="5*")
    tel = models.IntegerField(max_length=10)
    email = models.CharField(max_length=100)
    localisation = models.CharField(max_length=1000) 
    def __str__(self) :
        return self.nom

class Reservation(models.Model) : 
    date_reservation  = models.DateField( default=datetime.date.today)
    sejour = models.IntegerField() 
    voyage = models.ForeignKey(Voyage , on_delete=models.CASCADE)
    Transport = models.ForeignKey(Transport , on_delete = models.CASCADE , blank=True, null= True)
    Hotel = models.ForeignKey( Hotel, on_delete=models.CASCADE , blank=True, null= True)

