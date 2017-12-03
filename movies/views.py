# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.db import transaction
from django.contrib.auth.models import User
from .models import MovieInfo, MovieInfoManager, Review
from django.contrib.auth import authenticate, login
from imdb import IMDb
from collections import Counter
from django import forms
from .forms import SearchForm, ReviewForm
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
			#reviews = Review.objects. 
			#do something with reviews to prevent the review for the movie from going bye bye
			m.delete_all()
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
					titleSearch = movies['title']
					print titleSearch
					theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)
					#theMovieTwo = Movie.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)
					moviesData = MovieInfo.objects.filter(query=searchname) #modify this
				# if not theMovie:
				# 	moviesData = 'errorOne'
	 		# except:
				# moviesData = 'errorTwo'
				#moviesData = getMoviesData(searchname) 
		if 'p' in request.GET:
			titleKey = 'titles'
			ia = IMDb('http', useModule='lxml')
			m.delete_all()
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
					titleSearch = movies['title']
					print titleSearch
					theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)
					#theMovieTwo = Movie.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)

					moviesData = MovieInfo.objects.filter(query=searchname).order_by('title')
		if 'n' in request.GET:
			titleKey = 'titles'
			ia = IMDb('http', useModule='lxml')
			m.delete_all()
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
					titleSearch = movies['title']
					print titleSearch
					theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)
					moviesData = MovieInfo.objects.filter(query=searchname).order_by('-release_date')
			#moviesData = m.getMoviesInOrder(searchname)
		if request.GET.get('l') is not None:
			thaGenre = request.GET.get('l')
			thaGenre = thaGenre.lower()
			thaGenre = thaGenre.title()
			if 'g' in request.GET:
				#somelist = []
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
						titleSearch = movies['title']
						print titleSearch
						if thaGenre in somelist:
							theMovie = MovieInfo.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)
							#theMovieTwo = Movie.objects.create(title=titleSearch,movie_id=theID,genre=theGenre,release_date=theYear,rating=theRating, query=searchname, poster=posterOne, summary=plot, bigposter=posterTwo)
							moviesData = MovieInfo.objects.filter(query=searchname)
							count = count + 1
				if count == 0:
					moviesData = 'Genre does not match with title'
				#moviesData = m.getMoviesByGenre(searchname,genre)
		return render(request, 'search.html',{'moviesData': moviesData, 'search': True})
	else:
		return render(request, 'search.html')

def movie_page(request, movie_id):
	movie_pg = MovieInfo.objects.get(movie_id=movie_id)
	theUser = request.user
	print theUser.username
	#userReviews = Review.objects.filter(user=theUser)
	allReviews = Review.objects.filter(movie_id=movie_id)
	print allReviews
	if not allReviews:
		allReviews = 'No reviews yet'
	if request.GET:
		theComment = request.GET.get('review')
		print 'yuh'
		if 'moovify' in request.GET:
		 	theMovie = movie_pg
	 		theReview = Review.objects.create(movie_id=movie_id, user=theUser,comment=theComment)
	 		allReviews = Review.objects.filter(movie_id=movie_id)
	 		return render_to_response('movie.html',{'movie_pg':movie_pg, 'theUser':theUser, 'getReviews': allReviews})
 	#movie_pg = get_list_or_404(MovieInfo, movie_id=movie_id)
	else:
		return render_to_response('movie.html',{'movie_pg':movie_pg, 'theUser': theUser, 'getReviews': allReviews})




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
