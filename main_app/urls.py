from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_show, name='cats_show'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('cattoys/', views.cattoys_index, name='cattoys_index'),
    path('cattoys/<int:cattoy_id>', views.cattoys_show, name='cattoys_show'),
    path('cattoys/create/', views.CatToyCreate.as_view(), name='cattoys_create'),
    path('cattoys/<int:pk>/update/', views.CatToyUpdate.as_view(), name='cattoys_update'),
    path('cattoys/<int:pk>/delete/', views.CatToyDelete.as_view(), name='cattoys_delete'),
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>', views.associate_toy, name='associate_toy'),
    path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>', views.unassociate_toy, name='unassociate_toy'),


    path('summoners/', views.summoners_index, name='summoners_index'),
    path('summoners/<int:summoner_id>/',views.summoners_show , name='summoners_show'),
    path('summoners/create/', views.SummonerCreate.as_view(), name='summoners_create'),
    path('summoners/<int:pk>/update/', views.SummonerUpdate.as_view(), name='summoners_update'),
    path('summoners/<int:pk>/delete/', views.SummonerDelete.as_view(), name='summoners_delete'),


    path('matches/', views.matches_index, name='matches_index'),
    path('matches/<int:match_id>/',views.matches_show, name='matches_show'),
    path('matches/create/', views.MatchCreate.as_view(), name='matches_create'),
    path('matches/<int:pk>/update/', views.MatchUpdate.as_view(), name='matches_update'),
    path('matches/<int:pk>/delete/', views.MatchDelete.as_view(), name='matches_delete'),


    path('ranks/', views.ranks_index, name='ranks_index'),
    path('ranks/<int:rank_id>/',views.ranks_show, name='ranks_show'),
    path('ranks/create/', views.RankCreate.as_view(), name='ranks_create'),
    path('ranks/<int:pk>/update/', views.RankUpdate.as_view(), name='ranks_update'),

    path('search_summoner', views.search_summoner, name='search_summoner'),

]