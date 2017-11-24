# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import transaction
from .models import Movie, MovieInfo, MovieInfoManager
from imdb import IMDb
from collections import Counter
from django import forms
from .forms import SearchForm
from imdb import IMDb
from django.http import Http404, HttpResponse, HttpResponseRedirect
# Create your views here.
ia = IMDb()

m = MovieInfoManager()
def search(request):
	if request.GET:
		searchname = request.GET.get('q')
		if 'r' in request.GET:
			titleKey = 'titles'
			ia = IMDb('http', useModule='lxml')
			m.delete_all()
			for movies in ia.search_movie(searchname):
					theID = movies.movieID
					theRealDeal = ia.get_movie(theID)
					if 'genres' not in theRealDeal.keys():
						theGenre = 'NA'
					else:
						theGenre = theRealDeal['genres']
					if 'rating' not in theRealDeal.keys():
						theRating = 'No ratings yet'
					else:
						theRating = theRealDeal['rating']
					if 'year' not in theRealDeal.keys():
						theYear = 1000
					else:
						theYear = theRealDeal['year']
					titleSearch = movies['title']
					print titleSearch
					theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname)
					moviesData = MovieInfo.objects.filter(query=searchname) #modify this
				# if not theMovie:
				# 	moviesData = 'errorOne'
	 		# except:
				# moviesData = 'errorTwo'
				#moviesData = getMoviesData(searchname) 
		if 'p' in request.GET:
			moviesData = m.getMoviesAlphabetical(searchname)
		if 'n' in request.GET:
			moviesData = m.getMoviesInOrder(searchname)
		if request.GET.get('l') is not None:
			genre = request.GET.get('l')
			if 'g' in request.GET:
				moviesData = m.getMoviesByGenre(searchname,genre)
		return render(request, 'search.html',{'moviesData': moviesData, 'search': True})
	else:
		return render(request, 'search.html')

# def movie(request):
# 	if request.GET:
# 		if 'clicked' in request.GET:
			
# 	return render(request,'movie.html')


# def getMoviesData(titles): #use movie ID for all of these 
# 		theMovie = MovieInfo()
# 		titleKey = 'titles'
# 		ia = IMDb('http', useModule='lxml')
# 		try:
# 			for movies in ia.search_movie(titles):
# 				theID = movies.movieID
# 				theRealDeal = ia.get_movie(theID)
# 				if 'genres' not in theRealDeal.keys():
# 					theGenre = 'NA'
# 				else:
# 					theGenre = theRealDeal['genres']
# 				if 'rating' not in theRealDeal.keys():
# 					theRating = 'No ratings yet'
# 				else:
# 					theRating = theRealDeal['rating']
# 				if 'year' not in theRealDeal.keys():
# 					theYear = 1000
# 				else:
# 					theYear = theRealDeal['year']
# 				titleSearch = movies['title']
# 				theMovie = MovieInfo(title=titleSearch,movie_id=theID,genre=theGenre,release_date=year,rating=theRating)
# 				theMovie.save()
# 			if not theMovie:
# 				return 'errorOne'
# 			print theMovie
# 			return theMovie
# 		except:
# 			return 'errorTwo'
	

