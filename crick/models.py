
from typing import Match
from django.db import models

class players(models.Model):
    p_name=models.CharField(max_length=30)
    p_country=models.CharField(max_length=30)
    p_image=models.CharField(max_length=1000,null=True)

class tt(models.Model):
    player=models.ForeignKey(players,on_delete=models.CASCADE,null=True)
    runs=models.IntegerField(max_length=4)
    matches=models.IntegerField(max_length=4)
    hundreds=models.IntegerField(max_length=4)
    avg=models.FloatField(max_length=8)
    strikrate=models.FloatField(max_length=8)
    wickets=models.IntegerField(max_length=4)
    economy=models.FloatField(max_length=8)


    