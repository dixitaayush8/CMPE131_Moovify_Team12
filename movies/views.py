# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata
import random
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.db import transaction
from django.contrib.auth.models import User
from .models import MovieInfo, MovieInfoManager, Review
from django.contrib.auth import authenticate, login
from imdb import IMDb
from collections import Counter
from django import forms
from .forms import SearchForm, ReviewForm
from django.db.models import Avg
from imdb import IMDb
from django.http import Http404, HttpResponse, HttpResponseRedirect

ia = IMDb()

m = MovieInfoManager()
def search(request):
	if request.GET:
		searchname = request.GET.get('q')
		if 'r' in request.GET:
			titleKey = 'titles'
			ia = IMDb('http', useModule='lxml')
			m.delete_all()
			countOne = 0
			for movies in ia.search_movie(searchname):
					theID = movies.movieID
					theRealDeal = ia.get_movie(theID)
					if 'genres' not in theRealDeal.keys():
						theGenre = 'NA'
					else:
						somelist = [str(x) for x in theRealDeal['genres']]
						theGenre = ', '.join(somelist)
					if 'rating' not in theRealDeal.keys():
						theRating = 'No ratings yet'
					else:
						theRating = theRealDeal['rating']
					if 'year' not in theRealDeal.keys():
						theYear = 'Release date unknown'
					else:
						theYear = theRealDeal['year']
					if 'cover url' not in theRealDeal.keys():
						posterOne = 'http://www.cineart.be/Documents/Document/Large/20120510153359-NoPosterAvailable.jpg'
					else:
						posterOne = theRealDeal['cover url']
					if 'plot outline' not in theRealDeal.keys():
						plot = 'No plot available at this time'
					else:
						plot = theRealDeal['plot outline']
					if 'full-size cover url' not in theRealDeal.keys():
						posterTwo = 'http://www.cineart.be/Documents/Document/Large/20120510153359-NoPosterAvailable.jpg'
					else:
						posterTwo = theRealDeal['full-size cover url']
					if 'director' not in theRealDeal.keys():
						director = 'No director'
					else:
						director = theRealDeal['director'][0]
					if 'cast' not in theRealDeal.keys():
						cast = 'No cast'
					else:
						try:
							i=1
							cast = str(theRealDeal['cast'][0])
							if len(theRealDeal['cast']) > 0:
								while i < len(theRealDeal['cast']):
									#unOne = theRealDeal['cast'][i].decode('utf-8')
								#if isinstance(theRealDeal['cast'][i], str):
									cast = cast + ", " + str(theRealDeal['cast'][i])
								#elif isinstance(theRealDeal['cast'][i], unicode):
									#cast = cast + ", " + str(unicodedata.normalize('NFD', unOne).encode('ascii', 'ignore'))
									i = i + 1
						except UnicodeDecodeError:
							cast = "Could not retrieve cast"
					titleSearch = movies['title']
					theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo, director=director, cast=cast)
					#theMovieTwo = Movie.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)
					#print theMovie.title
					moviesData = MovieInfo.objects.filter(query=searchname)
					countOne = countOne + 1
			if countOne == 0:
				moviesData = "there is an error"
					#print type(moviesData)
				# if not theMovie:
				# 	moviesData = 'errorOne'
	 		# except:
				# moviesData = 'errorTwo'
				#moviesData = getMoviesData(searchname) 
		if 'p' in request.GET:
			titleKey = 'titles'
			ia = IMDb('http', useModule='lxml')
			m.delete_all()
			countTwo = 0
			for movies in ia.search_movie(searchname):
					theID = movies.movieID
					theRealDeal = ia.get_movie(theID)
					if 'genres' not in theRealDeal.keys():
						theGenre = 'NA'
					else:
						somelist = [str(x) for x in theRealDeal['genres']]
						theGenre = ', '.join(somelist)
					if 'rating' not in theRealDeal.keys():
						theRating = 'No ratings yet'
					else:
						theRating = theRealDeal['rating']
					if 'year' not in theRealDeal.keys():
						theYear = 'Release date unknown'
					else:
						theYear = theRealDeal['year']
					if 'cover url' not in theRealDeal.keys():
						posterOne = 'http://www.cineart.be/Documents/Document/Large/20120510153359-NoPosterAvailable.jpg'
					else:
						posterOne = theRealDeal['cover url']
					if 'plot outline' not in theRealDeal.keys():
						plot = 'No plot available at this time'
					else:
						plot = theRealDeal['plot outline']
					if 'full-size cover url' not in theRealDeal.keys():
						posterTwo = 'http://www.cineart.be/Documents/Document/Large/20120510153359-NoPosterAvailable.jpg'
					else:
						posterTwo = theRealDeal['full-size cover url']
					if 'director' not in theRealDeal.keys():
						director = 'No director'
					else:
						director = theRealDeal['director'][0]
					if 'cast' not in theRealDeal.keys():
						cast = 'No cast'
					else:
						try:
							i=1
							cast = str(theRealDeal['cast'][0])
							if len(theRealDeal['cast']) > 0:
								while i < len(theRealDeal['cast']):
									#unOne = theRealDeal['cast'][i].decode('utf-8')
								#if isinstance(theRealDeal['cast'][i], str):
									cast = cast + ", " + str(theRealDeal['cast'][i])
								#elif isinstance(theRealDeal['cast'][i], unicode):
									#cast = cast + ", " + str(unicodedata.normalize('NFD', unOne).encode('ascii', 'ignore'))
									i = i + 1
						except UnicodeDecodeError:
							cast = "Could not retrieve cast"
					titleSearch = movies['title']
					theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo, director = director, cast=cast)
					#theMovieTwo = Movie.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)

					moviesData = MovieInfo.objects.filter(query=searchname).order_by('title')
					countTwo = countTwo + 1
			if countTwo == 0:
				moviesData = "there is an error"
		if 'n' in request.GET:
			titleKey = 'titles'
			ia = IMDb('http', useModule='lxml')
			m.delete_all()
			countThree = 0
			for movies in ia.search_movie(searchname):
					theID = movies.movieID
					theRealDeal = ia.get_movie(theID)
					if 'genres' not in theRealDeal.keys():
						theGenre = 'NA'
					else:
						somelist = [str(x) for x in theRealDeal['genres']]
						theGenre = ', '.join(somelist)
					if 'rating' not in theRealDeal.keys():
						theRating = 'No ratings yet'
					else:
						theRating = theRealDeal['rating']
					if 'year' not in theRealDeal.keys():
						theYear = 'Release date unknown'
					else:
						theYear = theRealDeal['year']
					if 'cover url' not in theRealDeal.keys():
						posterOne = 'http://www.cineart.be/Documents/Document/Large/20120510153359-NoPosterAvailable.jpg'
					else:
						posterOne = theRealDeal['cover url']
					if 'plot outline' not in theRealDeal.keys():
						plot = 'No plot available at this time'
					else:
						plot = theRealDeal['plot outline']
					if 'full-size cover url' not in theRealDeal.keys():
						posterTwo = 'http://www.cineart.be/Documents/Document/Large/20120510153359-NoPosterAvailable.jpg'
					else:
						posterTwo = theRealDeal['full-size cover url']
					if 'director' not in theRealDeal.keys():
						director = 'No director'
					else:
						director = theRealDeal['director'][0]
					if 'cast' not in theRealDeal.keys():
						cast = 'No cast'
					else:
						try:
							i=1
							cast = str(theRealDeal['cast'][0])
							if len(theRealDeal['cast']) > 0:
								while i < len(theRealDeal['cast']):
									#unOne = theRealDeal['cast'][i].decode('utf-8')
								#if isinstance(theRealDeal['cast'][i], str):
									cast = cast + ", " + str(theRealDeal['cast'][i])
								#elif isinstance(theRealDeal['cast'][i], unicode):
									#cast = cast + ", " + str(unicodedata.normalize('NFD', unOne).encode('ascii', 'ignore'))
									i = i + 1
						except UnicodeDecodeError:
							cast = "Could not retrieve cast"
					titleSearch = movies['title']
					theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo, director=director, cast=cast)
					moviesData = MovieInfo.objects.filter(query=searchname).order_by('-release_date')
					countThree = countThree + 1
			if countThree == 0:
				moviesData = "there is an error"
		if request.GET.get('l') is not None:
			thaGenre = request.GET.get('l')
			thaGenre = thaGenre.lower()
			thaGenre = thaGenre.title()
			if 'g' in request.GET:
				count = 0
				titleKey = 'titles'
				ia = IMDb('http', useModule='lxml')
				m.delete_all()
				for movies in ia.search_movie(searchname):
						theID = movies.movieID
						theRealDeal = ia.get_movie(theID)
						if 'genres' not in theRealDeal.keys():
							theGenre = 'NA'
							somelist = ['NA']
						else:
							somelist = [str(x) for x in theRealDeal['genres']]
							theGenre = ', '.join(somelist)
						if 'rating' not in theRealDeal.keys():
							theRating = 'No ratings yet'
						else:
							theRating = theRealDeal['rating']
						if 'year' not in theRealDeal.keys():
							theYear = 'Release date unknown'
						else:
							theYear = theRealDeal['year']
						if 'cover url' not in theRealDeal.keys():
							posterOne = 'http://www.cineart.be/Documents/Document/Large/20120510153359-NoPosterAvailable.jpg'
						else:
							posterOne = theRealDeal['cover url']
						if 'plot outline' not in theRealDeal.keys():
							plot = 'No plot available at this time'
						else:
							plot = theRealDeal['plot outline']
						if 'full-size cover url' not in theRealDeal.keys():
							posterTwo = 'http://www.cineart.be/Documents/Document/Large/20120510153359-NoPosterAvailable.jpg'
						else:
							posterTwo = theRealDeal['full-size cover url']
						if 'director' not in theRealDeal.keys():
							director = 'No director'
						else:
							director = theRealDeal['director'][0]
						if 'cast' not in theRealDeal.keys():
							cast = 'No cast'
						else:
							try:
								i=1
								cast = str(theRealDeal['cast'][0])
								if len(theRealDeal['cast']) > 0:
									while i < len(theRealDeal['cast']):
										#unOne = theRealDeal['cast'][i].decode('utf-8')
									#if isinstance(theRealDeal['cast'][i], str):
										cast = cast + ", " + str(theRealDeal['cast'][i])
									#elif isinstance(theRealDeal['cast'][i], unicode):
										#cast = cast + ", " + str(unicodedata.normalize('NFD', unOne).encode('ascii', 'ignore'))
										i = i + 1
							except UnicodeDecodeError:
								cast = "Could not retrieve cast"
						titleSearch = movies['title']
						if thaGenre in somelist:
							theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo, director=director, cast=cast)
							#theMovieTwo = Movie.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)
							moviesData = MovieInfo.objects.filter(query=searchname)
							count = count + 1
				if count == 0:
					moviesData = 'Genre does not match with title'
		return render(request, 'search.html',{'moviesData': moviesData, 'search': True})
	else:
		return render(request, 'search.html')

def movie_page(request, movie_id):
	movie_pg = MovieInfo.objects.get(movie_id=movie_id)
	theUser = request.user
	k = ia.get_movie(movie_pg.movie_id)
	theMovieTitle = str(k)
	allReviews = Review.objects.filter(movie_id=movie_id)
	average = allReviews.aggregate(Avg('rating'))
	if not allReviews:
		allReviews = 'No reviews yet'
	if request.GET:
		theComment = request.GET.get('review')
		theRating = request.GET.get('number')
		if 'moovify' in request.GET:
		 	theMovie = movie_pg
	 		theReview = Review.objects.create(movie_id=movie_id, user=theUser,comment=theComment, movie_title=theMovieTitle,rating=theRating)
	 		allReviews = Review.objects.filter(movie_id=movie_id)
	 		average = allReviews.aggregate(Avg('rating'))
	 		return render_to_response('movie.html',{'movie_pg':movie_pg, 'theUser':theUser, 'getReviews': allReviews, 'average': average})
	else:
		return render_to_response('movie.html',{'movie_pg':movie_pg, 'theUser': theUser, 'getReviews': allReviews, 'average': average})

def list_reviews(request):
	theUser = request.user
	review_pg = Review.objects.filter(user=theUser)
	if not review_pg:
		review_pg = 'nope'
	return render_to_response('review_list.html',{'review_pg': review_pg})

def suggested(request):
	movieResults = []
	movies = []
	theUser = request.user
	reviews = Review.objects.filter(user=theUser)
	if not reviews:
		movies = 'Nonexistent'
	for r in reviews:
		if r.rating > 5:
			for i in ia.search_movie(r.movie_title):
				if len(i['title']) < 50:
					movieResults.append(i['title'])
			movieResults.remove(r.movie_title)
			theResults = list(set(movieResults))
			movies.append(random.choice(theResults))
	return render_to_response('suggested.html',{'movies': movies})
