from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('summoner/', include('summoner.url')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]