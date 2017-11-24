# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from imdb import IMDb

from collections import Counter

class Movie(models.Model):
	titles = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)

	# def getMoviesData(self,titles): #use movie ID for all of these 
	# 	theMovie = MovieInfo()
	# 	titleKey = 'titles'
	# 	ia = IMDb('http', useModule='lxml')
	# 	try:
	# 		for movies in ia.search_movie(titles):
	# 			theID = movies.movieID
	# 			theRealDeal = ia.get_movie(theID)
	# 			if 'genres' not in theRealDeal.keys():
	# 				theGenre = 'NA'
	# 			else:
	# 				theGenre = theRealDeal['genres']
	# 			if 'rating' not in theRealDeal.keys():
	# 				theRating = 'No ratings yet'
	# 			else:
	# 				theRating = theRealDeal['rating']
	# 			if 'year' not in theRealDeal.keys():
	# 				theYear = 1000
	# 			else:
	# 				theYear = theRealDeal['year']
	# 			titleSearch = movies['title']
	# 			theMovie = MovieInfo(title=titleSearch,movie_id=theID,genre=theGenre,release_date=year,rating=theRating)
	# 			theMovie.save()
	# 		if not theMovie:
	# 			return 'errorOne'
	# 		print theMovie
	# 		return theMovie
	# 	except:
	# 		return 'errorTwo'


	def getMoviesAlphabetical(self,titles):
		self.moviesData = {}
		titleKey = 'titles'
		ia = IMDb('http', useModule='lxml')
		try:
			for movies in ia.search_movie(titles):
				titleSearch = movies['title']
				self.moviesData.setdefault(titleKey, []).append(titleSearch)
			if not self.moviesData:
				return 'errorOne'
			self.moviesData['titles'].sort()
			return self.moviesData
		except:
			return 'errorTwo'

	def getMoviesInOrder(self,titles):
		newDic = []
		newDicTwo = []
		someList = []
		someDic = {}
		dic = {}
		tup = ()
		listOne = []
		listTwo = []
		listThree = []
		listFour = []
		ia = IMDb('http', useModule='lxml')
		for movies in ia.search_movie(titles):
			someMovie = movies['title']
			yolo = movies.movieID
			lala = ia.get_movie(yolo)
			if 'year' not in lala.keys():
				theYear = 1000
			else:
				theYear = lala['year']
			listThree.append(theYear)
			listOne.append(someMovie)
			listTwo.append(yolo)
		newList = zip(listOne, listTwo)
		newerList = zip(newList,listThree)
		d = dict(newerList)
		c = Counter(d)
		di = c.most_common()
		i = 0
		while i < len(di):
			newDic.append(di[i][0][0])
			newDic.append(di[i][0][1])
			newDicTwo.append(newDic)
			i+=1
			newDic = []
		return newDicTwo

	# def getMoviesInOrder(self,title): 
	# 	self.moviesData = {}
	# 	self.updatedList = {}
	# 	titleKey = 'titles'
	# 	yearKey = 'years'
	# 	ia = IMDb('http', useModule='lxml')
	# 	try:
	# 		for movies in ia.search_movie(title):
	# 			theID = movies.movieID #append movie title to key of list, use tuples and make dictionary of tuples
	# 			idList.append(theID)
	# 			theRealDeal = ia.get_movie(theID)
	# 			if 'year' not in theRealDeal.keys():
	# 				theYear = 1000
	# 			else:
	# 				theYear = theRealDeal["year"]
	# 			titleSearch = movies['title']
	# 			self.updatedList[titleSearch] = theYear
	# 		print idList
	# 		c = Counter(self.updatedList)
	# 		idList.sort()
	# 		someDict = c.most_common()
	# 		i = 0
	# 		while i < len(someDict):
	# 			self.moviesData.setdefault(titleKey,[]).append(someDict[i][0])
	# 			self.moviesData[someDict[i][0]] = theID
	# 			i+=1
	# 		print self.moviesData
	# 		if not self.moviesData:
	# 			return 'nah'
	# 		return self.moviesData
	# 	except:
	# 		return 'yoyo'

	def getMoviesByGenre(self,titles,genre):
		genre = genre.lower()
		genre = genre.title()
		someList = {}
		updatedList = {}
		self.moviesData = {}
		titleKey = 'titles'
		genreKey = 'genres'
		ia = IMDb('http', useModule='lxml')
		try:
			for movies in ia.search_movie(titles):
				theID = movies.movieID
				theRealDeal = ia.get_movie(theID)
				if 'genres' not in theRealDeal.keys():
					theGenre = 'NA'
				else:
					theGenre = theRealDeal["genres"]
				titleSearch = movies['title']
				updatedList[titleSearch] = theGenre
			print updatedList
			for n in updatedList:
				if genre in updatedList[n]:
					self.moviesData.setdefault(titleKey,[]).append(n)
			if not self.moviesData:
				return 'Genre does not match with the movie.'
			return self.moviesData
		except:
			return 'errorTwo'

class MovieInfo(models.Model):
	title = models.CharField(max_length=100)
	movie_id = models.CharField(max_length=10)
	genre = models.CharField(max_length=100)
	release_date = models.CharField(max_length=100)
	rating = models.CharField(max_length = 10)
	query = models.CharField(max_length = 100, default='')
	poster = models.CharField(max_length = 100, default='No poster available')

class MovieInfoManager(models.Manager):
	def delete_all(self):
		MovieInfo.objects.all().delete()





