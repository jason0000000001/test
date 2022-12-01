from unicodedata import name
from django.db import models

# Create your models here.
'''
class Room(models.Model):
    image_id = models.IntegerField(db_column='imageid', default = True)
    name = models.CharField(max_length=45)
    #description = models.TextField(blank=True, null=True)
    birthday = models.CharField(max_length=45, default = True)
    sex = models.CharField(max_length=45, default = True)
    temperature = models.FloatField(default = True)
    weight = models.FloatField(default = True)
    height = models.IntegerField(default = True)
    pressures = models.IntegerField(db_column='pressureS', default = True)
    pressured = models.IntegerField(db_column='pressureD', default = True)
    #updated = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)
'''
class Room(models.Model):
    image_id = models.IntegerField(db_column='imageid', default = 0)
    name = models.CharField(max_length=45)
    #description = models.TextField(blank=True, null=True)
    birthday = models.CharField(max_length=45, default = "2002/07/11")
    sex = models.CharField(max_length=45, default = "male")
    temperature = models.FloatField(default = 0)
    weight = models.FloatField(default = 0)
    height = models.FloatField(default = 0)
    pressures = models.IntegerField(db_column='pressureS', default = 0)
    pressured = models.IntegerField(db_column='pressureD', default = 0)
    #updated = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name