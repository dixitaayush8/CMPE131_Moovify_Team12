from django.conf.urls import url, include
from django.contrib import admin
from movies import views
from .views import search
urlpatterns = [
	url(r'^search/', search)
]