import datetime
from nis import match

from django.contrib.postgres.fields import ArrayField

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Summoner(models.Model):
    ### summoner v4 ### summoner name
    summoner_name = models.CharField(max_length=32)
    id = models.CharField(max_length=63)
    puuid = models.CharField(max_length=78)
    account_id = models.CharField(max_length=56)
    profile_icon_id = models.IntegerField()
    
    summoner_level = models.IntegerField()
    ### match v5 ### need puuid ### gets the match ids in a list of strings
    match_id_list = models.ArrayField(
        models.CharField(max_length=225)
    )
    ### match v5 ### need the match id from above
    game_mode = models.CharField()


    kill_count = models.IntegerField()
    death_count = models.IntegerField()
    assist_count = models.IntegerField()
    #### above is api stuff
    profile_picture = models.ImageField()
    rateing = models.IntegerField(default=2)
    comment_text = models.CharField(max_length=144)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.summoner_name
    def __str__(self):
        return self.comment_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Team(models.Model):
    searched_summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE) ## this is the one you searched
    summoner_1 = models.CharField(max_length=32)
    summoner_2 = models.CharField(max_length=32)
    summoner_3 = models.CharField(max_length=32)
    summoner_4 = models.CharField(max_length=32)
    summoner_5 = models.CharField(max_length=32)
    summoner_6 = models.CharField(max_length=32)
    summoner_7 = models.CharField(max_length=32)
    summoner_8 = models.CharField(max_length=32)
    summoner_9 = models.CharField(max_length=32)
    def __str__(self):
        return self.summoner_1
    def __str__(self):
        return self.searched_summoner
