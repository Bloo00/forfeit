from curses.ascii import HT
from dataclasses import field
from urllib import request
from xml.parsers.expat import model
from django.shortcuts import render, redirect,get_object_or_404
from .models import Cat, CatToy, Summoner, Match, Rank, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

########### USER #############
def login_view(request):
    if request.method == 'POST':
        # try to log the user in
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user) # log the user in by creating a session
                    return redirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return redirect('/login')
        else:
            print('The username and/or password is incorrect.')
            return redirect('/login')
    else: # it was a GET request so send the empty login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/user/'+str(user))
        else:
            return HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username,'cats': cats})

############# CATS ###############

# django will make a create cat form for us!
@method_decorator(login_required, name='dispatch')
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print('!!!!! SELF.OBJECT:', self.object)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cats')

### Summoner
@method_decorator(login_required, name='dispatch')
class SummonerCreate(CreateView):
    model = Summoner
    fields = '__all__'
    success_url = "/summoners/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print("self.object: ",self.object)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect("/summoners")

### Match
@method_decorator(login_required, name='dispatch')
class MatchCreate(CreateView):
    model = Match
    fields = '__all__'
    success_url = "/matches/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print("self.object: ",self.object)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect("/matches")

### Rank
@method_decorator(login_required, name='dispatch')
class RankCreate(CreateView):
    model = Rank
    fields = '__all__'
    success_url = "/ranks/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print("self.object: ",self.object)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect("/ranks")

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form): # this will allow us to catch the pk to redirect to the show page
        self.object = form.save(commit=False) # don't post to the db until we say so
        self.object.save()
        return HttpResponseRedirect('/cats/'+str(self.object.pk))

### Summoner
class SummonerUpdate(UpdateView):
    model = Summoner
    fields = ["summoner_name","summoner_lvl","solo_rank","flex_rank","profile_icon"]

    def form_valid(self, form): # this will allow us to catch the pk to redirect to the show page
        self.object = form.save(commit=False) # don't post to the db until we say so
        self.object.save()
        return HttpResponseRedirect('/summoners/'+str(self.object.pk))

### Match
class MatchUpdate(UpdateView):
    model = Match
    fields = "__all__"

    def form_valid(self, form): # this will allow us to catch the pk to redirect to the show page
        self.object = form.save(commit=False) # don't post to the db until we say so
        self.object.save()
        return HttpResponseRedirect('/matches/'+str(self.object.pk))

### Rank
class RankUpdate(UpdateView):
    model = Rank
    fields = "__all__"

    def form_valid(self, form): # this will allow us to catch the pk to redirect to the show page
        self.object = form.save(commit=False) # don't post to the db until we say so
        self.object.save()
        return HttpResponseRedirect('/ranks/'+str(self.object.pk))


class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'

### Summoner
class SummonerDelete(DeleteView):
    model = Summoner
    success_url = '/summoners'

### Match
class MatchDelete(DeleteView):
    model = Match
    success_url = '/matches'

### Rank
class RankDelete(DeleteView):
    model = Rank
    success_url = '/ranks'

def cats_index(request):
    # Get all cats from the db
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

### Summoners

def summoners_index(request):
    # Get all cats from the db
    summoners = Summoner.objects.all()
    return render(request, 'summoners/index.html', {'summoners': summoners})

## Match
def matches_index(request):
    # Get all cats from the db
    matches = Match.objects.all()
    return render(request, 'matches/index.html', {'matches': matches})

## Rank
def ranks_index(request):
    # Get all cats from the db
    ranks = Rank.objects.all()
    return render(request, 'ranks/index.html', {'ranks': ranks})

    
def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    toys = CatToy.objects.all()
    return render(request, 'cats/show.html', {'cat': cat, 'toys': toys})

### Summoner

def summoners_show(request, summoner_id):
    summoner = Summoner.objects.get(id=summoner_id)
    return render(request, 'summoners/show.html', {'summoner': summoner})

### Match

def matches_show(request, match_id):
    match = Match.objects.get(id=match_id)
    return render(request, 'matches/show.html', {'match': match})

### Rank

def ranks_show(request, rank_id):
    rank = Rank.objects.get(id=rank_id)
    summoner = Summoner.objects.all()
    return render(request, 'ranks/show.html', {'rank': rank,'summoner':summoner})

########### DEFAULT ###################

def index(request):
    return render(request, 'index.html')
  

def about(request):
    return render(request, 'about.html')

def search_summoner(request):
    if request.method == "POST":
        searched = request.POST['searched']
        summoner = Summoner.objects.all().filter(summoner_name__contains=searched)
        return render(request,"summoner/search_summoner.html",{'searched':searched,'summoner':summoner})
    else:
        return render(request,"summoner/search_summoner.html",{})


######### comments/rateing #######

@method_decorator(login_required, name='dispatch')
def comment_create(request):
    model = Comment
    fields = ['body']
    success_url = "/matches/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print("self.object: ",self.object)
        self.object.user = self.request.user
        self.object.save()
        self.object.author = request.user
        return HttpResponseRedirect("/matches")

########## CATTOYS ################

def cattoys_index(request):
    cattoys = CatToy.objects.all()
    return render(request, 'cattoys/index.html', {'cattoys': cattoys})

def cattoys_show(request, cattoy_id):
    cattoy = CatToy.objects.get(id=cattoy_id)
    return render(request, 'cattoys/show.html', {'cattoy': cattoy})

class CatToyCreate(CreateView):
    model = CatToy
    fields = '__all__'
    success_url = '/cattoys'

class CatToyUpdate(UpdateView):
    model = CatToy
    fields = ['name', 'color']
    success_url = '/cattoys'

class CatToyDelete(DeleteView):
    model = CatToy
    success_url = '/cattoys'

def associate_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).cattoys.add(toy_id)
    # return HttpResponseRedirect('/cats/'+str(cat_id)+'/')
    return redirect('cats_show', cat_id=cat_id)

def unassociate_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).cattoys.remove(toy_id)
    return HttpResponseRedirect('/cats/'+str(cat_id)+'/')