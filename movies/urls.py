from django.conf.urls import url, include
from django.contrib import admin
from movies import views
from .views import search, movie_page, list_reviews
from .models import MovieInfo


urlpatterns = [
	url(r'^search/', search),
	#url(r'^movie/$', views.movie_page,name='movie_page'),
	url(r'^review_list/', list_reviews),
	url(r'^movie/(?P<movie_id>\d+)/$',movie_page),
]