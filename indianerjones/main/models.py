from datetime import datetime
from django.db import models

class Country(models.Model):
    name = models.CharField(verbose_name="Name of the country", max_length=250)
    flag = models.ImageField(verbose_name="Image of the country flag", upload_to='country_flags', blank=True)

    def __unicode__(self):
        return self.name

class University(models.Model):
    name = models.CharField(verbose_name="Name of the University", max_length=250)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(verbose_name="Name of the department", max_length=250)
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(verbose_name="Short name", max_length=50)
    url = models.URLField(verbose_name="URL")

    def __unicode__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(verbose_name="Fist name", max_length=50)
    middle_name = models.CharField(verbose_name="Middle name", max_length=50, blank=True)
    last_name = models.CharField(verbose_name="Last name", max_length=50)
    publish_date = models.IntegerField(max_length=4, default=lambda: datetime.now().year , verbose_name="Publishing date")
    title = models.CharField(verbose_name="Title of the dissertation", max_length=250)
    subtitle = models.CharField(verbose_name="Subtitle of the dissertation", max_length=250, blank=True)
    isbn = models.CharField(verbose_name="ISBN", max_length=13, blank=True)
    department = models.ForeignKey(Department)
    adviser = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __unicode__(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name
