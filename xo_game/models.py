from django.db import models

# Create your models here.


class Game(models.Model):
    gameid = models.CharField(max_length=100, null=True, blank=True)
    player1 = models.CharField(max_length=100, null=True, blank=True)
    player2 = models.CharField(max_length=100, null=True, blank=True)
    turn = models.CharField(max_length=1, null=True, blank=True)
    player1_symbol = models.CharField(max_length=1, null=True, blank=True)
    player2_symbol = models.CharField(max_length=1, null=True, blank=True)
    box1 = models.CharField(max_length=1, null=True, blank=True)
    box2 = models.CharField(max_length=1, null=True, blank=True)
    box3 = models.CharField(max_length=1, null=True, blank=True)
    box4 = models.CharField(max_length=1, null=True, blank=True)
    box5 = models.CharField(max_length=1, null=True, blank=True)
    box6 = models.CharField(max_length=1, null=True, blank=True)
    box7 = models.CharField(max_length=1, null=True, blank=True)
    box8 = models.CharField(max_length=1, null=True, blank=True)
    box9 = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.gameid
