from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=250)
    flag = models.ImageField(upload_to='country_flags')

class University(models.Model):
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country)

class Department(models.Model):
    name = models.CharField(max_length=250)
    university = models.ForeignKey(University)

class Link(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    publish_date = models.DateField()
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    department = models.ForeignKey(Department)
    adviser = models.ManyToManyField("self", blank=True)
