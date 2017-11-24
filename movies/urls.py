from django.conf.urls import url, include
from django.contrib import admin
from movies import views
from .views import search
from .models import MovieInfo 


urlpatterns = [
	url(r'^search/', search),
]