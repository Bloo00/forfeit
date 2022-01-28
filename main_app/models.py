from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class CatToy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cattoys = models.ManyToManyField(CatToy)

    def __str__(self):
        return self.name

class Summoner(models.Model):
    id = models.AutoField(primary_key=True)
    summoner_name = models.CharField(max_length=36)
    summoner_lvl = models.IntegerField()
    solo_rank = models.CharField(max_length=15)
    flex_rank = models.CharField(max_length=15)
    win_rate = models.IntegerField()
    riot_id = models.CharField(max_length=63)
    puuid = models.CharField(max_length=78)
    account_id = models.CharField(max_length=56)
    profile_icon_id = models.IntegerField()
    profile_icon = models.ImageField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    items = ArrayField(
        models.CharField(max_length=32),
        size = 7,
    )
    game_lvl = models.IntegerField()
    creep_score = models.IntegerField()

    def __str__(self):
        return self.summoner_name

class Match(models.Model):
    id = models.AutoField(primary_key=True)
    summoner = models.ForeignKey(Summoner,on_delete=models.CASCADE)
    game_type = models.CharField(max_length=32)
    win_loss = models.BooleanField()
    game_length = models.DurationField()
    blue_dragons_taken = models.IntegerField()
    blue_barons_taken = models.IntegerField()
    blue_towers_taken = models.IntegerField()
    blue_gold_total = models.IntegerField()
    red_dragons_taken = models.IntegerField()
    red_barons_taken = models.IntegerField()
    red_towers_taken = models.IntegerField()
    red_gold_total = models.IntegerField()

class Rank(models.Model):
    id = models.AutoField(primary_key=True)
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    solo_duo_rank = models.CharField(max_length=32)
    rank_icon = models.ImageField()
    flex_rank = models.IntegerField()
    win_count = models.IntegerField()
    loss_count = models.IntegerField()
    lp = models.IntegerField()
