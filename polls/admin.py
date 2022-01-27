from django.contrib import admin

from .models import Question, Summoner, Team

admin.site.register(Question)
admin.site.register(Summoner)
admin.site.register(Team)