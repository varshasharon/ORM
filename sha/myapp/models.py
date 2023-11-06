from django.db import models
from django.contrib import admin
class Player (models.Model):
    PlayerID=models.CharField(max_length=20,help_text="Player ID")
    PlayerName=models.CharField(max_length=100)
    JerseyNumber=models.IntegerField()
    Age=models.IntegerField()
    Email=models.EmailField()

class PlayerAdmin(admin.ModelAdmin):
    list_display=('PlayerID','PlayerName','JerseyNumber','Age','Email')
