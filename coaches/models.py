from django.db import models
from players.models import Player

TYPES = [
                ('BAT', 'batting'),
                ('BOWL', 'bowling'),
                ('FIELD', 'fielding'),
                ('FIT', 'fitness')
            ]


class Training(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    training_type = models.CharField(choices = TYPES, max_length=10)
    start = models.TimeField()
    end = models.TimeField()
    date = models.DateField()



