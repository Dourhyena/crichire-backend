from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Player(models.Model):
    
    TYPE = [('BAT', 'batsmen'),
            ('BOWL', 'bowler'),
            ('ALR', 'all rounder')]
    jersey = models.PositiveIntegerField(unique = True)
    name = models.CharField(max_length=20)
    role = models.CharField(choices=TYPE, max_length = 12)

    def __str__(self):
        return self.name

class Player_Stats(models.Model):
    MATCH_TYPE = [('ODI', 'One Day'),
                   ('T20', 'Twenty'),
                    ('TST', 'Test')]
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name = "stats")
    match_type = models.CharField(choices = MATCH_TYPE, max_length = 7)
    strike_rate = models.DecimalField(max_digits=5, decimal_places=2)
    wickets = models.PositiveSmallIntegerField()
    runs = models.PositiveIntegerField()
    is_available = models.BooleanField()
    economy = models.FloatField()

class Fixture(models.Model):
    MATCH_TYPE = [('ODI', 'One Day'),
                    ('T20', 'Twenty'),
                    ('TST', 'Test')]
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=50)
    opposition = models.CharField(max_length=50)
    match_type =  models.CharField(choices = MATCH_TYPE, max_length = 7)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, default = 1)


class CompletePlayer(models.Model):
    player_id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    match_type = models.CharField(max_length=25)
    strike_rate = models.DecimalField(max_digits=5, decimal_places=2)
    wickets = models.PositiveSmallIntegerField()
    runs = models.PositiveIntegerField()
    is_available = models.BooleanField()
    economy = models.FloatField()





    



