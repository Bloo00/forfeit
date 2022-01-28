from pyexpat import model
from django.shortcuts import render, redirect
from .models import Cat, CatToy, Summoner, Match, Rank 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, response
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from dotenv import load_dotenv 
import os 

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
    return redirect('/cats')

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
import requests

#### Summoner ####
@method_decorator(login_required, name='dispatch')

class summoner_index(CreateView):
    model = Summoner
    fields = 'summoner_name'
    success_url = '/summoner/'
   
    def form_valid(self, form):
        print(form)
        self.object =  form.save(commit=False)
        print('!!!!! SELF.OBJECT:', self.object)
        self.object.user = self.request.user
        self.object.save()
        def get_summoner_by_name(name):
            load_dotenv()
            key = os.environ.get('RIOT_API')
            try:
                response = requests.get(f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={key}")
                print(response)
                return HttpResponseRedirect('/summoner')
            except:
                return HttpResponseRedirect('/index') #make 404
            
def Summoner(request):
    # show yourself
    ""


########### DEFAULT ###################
# import requests
# class index(request):
#     model = Summoner
#     fields = '__all__'
#     success_url = '/summoner/'

#     def form_valid(self, form):
#         self.object =  form.save(commit=False)
#         print('!!!!! SELF.OBJECT:', self.object)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect('/summoner')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
