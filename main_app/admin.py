from nis import match
from django.contrib import admin
from .models import Cat, CatToy, Comment, Summoner, Rank, Match

# Register your models here.
admin.site.register(Cat)
admin.site.register(CatToy)
admin.site.register(Summoner)
admin.site.register(Rank)
admin.site.register(Match)
admin.site.register(Comment)