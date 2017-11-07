# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from imdb import IMDb

from collections import Counter

class Movie(models.Model):
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)

	def getMoviesData(self,title):
		self.moviesData = {}
		titleKey = 'titles'
		ia = IMDb('http', useModule='lxml')
		for movies in ia.search_movie(title):
			titleSearch = movies['title']
			self.moviesData.setdefault(titleKey, []).append(titleSearch)
		return self.moviesData['titles']

	def getMoviesAlphabetical(self,title):
		self.moviesData = {}
		titleKey = 'titles'
		ia = IMDb('http', useModule='lxml')
		for movies in ia.search_movie(title):
			titleSearch = movies['title']
			self.moviesData.setdefault(titleKey, []).append(titleSearch)
		self.moviesData['titles'].sort()
		return self.moviesData['titles']

	def getMoviesInOrder(self,title): 
		self.moviesData = {}
		self.updatedList = {}
		titleKey = 'titles'
		yearKey = 'years'
		ia = IMDb('http', useModule='lxml')
		for movies in ia.search_movie(title):
			theID = movies.movieID
			theRealDeal = ia.get_movie(theID)
			if 'year' not in theRealDeal.keys():
				theYear = 1000
			else:
				theYear = theRealDeal["year"]
			titleSearch = movies['title']
			self.updatedList[titleSearch] = theYear
		c = Counter(self.updatedList)
		someDict = c.most_common()
		i = 0
		while i < len(someDict):
			self.moviesData.setdefault(titleKey,[]).append(someDict[i][0])
			i+=1
		return self.moviesData['titles']

	def getMoviesByGenre(self,title,genre):
		genre = genre.lower()
		genre = genre.title()
		someList = {}
		updatedList = {}
		self.moviesData = {}
		titleKey = 'titles'
		genreKey = 'genres'
		ia = IMDb('http', useModule='lxml')
		for movies in ia.search_movie(title):
			theID = movies.movieID
			theRealDeal = ia.get_movie(theID)
			if 'genres' not in theRealDeal.keys():
				theGenre = 'NA'
			else:
				theGenre = theRealDeal["genres"]
			titleSearch = movies['title']
			updatedList[titleSearch] = theGenre
		for n in updatedList:
			if genre in updatedList[n]:
				self.moviesData.setdefault(titleKey,[]).append(n)
		if not self.moviesData:
			return 'Genre does not match with the movie.'
		return self.moviesData['titles']


