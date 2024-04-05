# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
'''
admin.py
from django.contrib import admin
from .models import game
admin.site.register(game)

models.py

from django.db import models

class game(models.Model):
    gameid = models.IntegerField()
    gamename= models.CharField(max_length=20)
    gamelevel = models.CharField(max_length=20)
    gamescore = models.CharField(max_length=20)
'''

## OUTPUT

![output](./webmap.png)
![output](./web.png)
![output](./web1.png)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
