# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Movie
from django import forms
from .forms import SearchForm
from imdb import IMDb
from django.http import Http404, HttpResponse, HttpResponseRedirect
# Create your views here.
ia = IMDb()

m = Movie()
def search(request):
	if request.GET:
		searchname = request.GET.get('q')
		if 'r' in request.GET:
			moviesData = m.getMoviesData(searchname) 
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
