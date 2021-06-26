from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    continent = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    division = models.CharField(max_length=250, blank=True, null=True)
    district = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    road_or_streetNo = models.CharField(max_length=250, blank=True, null=True)
    policestation = models.CharField(max_length=250, blank=True, null=True)
    postoffice = models.CharField(max_length=250, blank=True, null=True)
    zipcode = models.CharField(max_length=250, blank=True, null=True)
    upozila_thana = models.CharField(max_length=250, blank=True, null=True)
    municipality = models.CharField(max_length=250, blank=True, null=True)
    union = models.CharField(max_length=250, blank=True, null=True)
    word_no = models.CharField(max_length=250, blank=True, null=True)
    village = models.CharField(max_length=250, blank=True, null=True)
    mahalla = models.CharField(max_length=250, blank=True, null=True)
    block = models.CharField(max_length=250, blank=True, null=True)
    holdingNo = models.CharField(max_length=250, blank=True, null=True)
    house = models.CharField(max_length=250, blank=True, null=True)

class Continent(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name



class State(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name


class Road_or_Street_No(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name


class PoliceStation(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name


class PostOffice(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class PostCode_or_ZipCode(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class ThanaUpozila(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class Union(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class WordNo(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class Mahalla(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name


class HoldingNo(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name
class House(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name


