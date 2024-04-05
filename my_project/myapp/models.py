from django.db import models

# Create your models here.
class game(models.Model):
    gameid = models.IntegerField()
    gamename= models.CharField(max_length=20)
    gamelevel = models.CharField(max_length=20)
    gamescore = models.CharField(max_length=20)