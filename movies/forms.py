from django import forms

class SearchForm(forms.Form):
	movie = forms.CharField(
		required = True,
		label = 'Movie',
		max_length = 100
		)