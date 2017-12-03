# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

from imdb import IMDb

class MovieInfo(models.Model):
	title = models.CharField(max_length=100)
	movie_id = models.CharField(max_length=10, primary_key=True)
	genre = models.CharField(max_length=100)
	release_date = models.CharField(max_length=100)
	rating = models.CharField(max_length = 10)
	query = models.CharField(max_length = 100, default='')
	poster = models.CharField(max_length = 100, default='No poster available')
	summary = models.CharField(max_length = 200, default='No summary at this time')
	bigposter = models.CharField(max_length = 300, default='No poster available')
	director = models.CharField(max_length = 200, default='No director')
	cast = models.CharField(max_length = 2000, default='No cast')


class Review(models.Model):
	movie_id = models.CharField(max_length=10)
	user = models.ForeignKey(User)
	comment = models.TextField()
	movie_title = models.CharField(max_length=100, default='')
	rating = models.FloatField(max_length=2, default=1)
	def __str__(self):
		return self.comment

class MovieInfoManager(models.Manager):
	def delete_all(self):
		MovieInfo.objects.all().delete()






