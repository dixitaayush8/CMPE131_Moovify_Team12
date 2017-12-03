from django import forms

class SearchForm(forms.Form):
	movie = forms.CharField(
		required = True,
		label = 'Movie',
		max_length = 100
		)

class ReviewForm(forms.Form):
	review = forms.CharField(
		widget = forms.Textarea,
		required = True,
		label = 'Review',
		)
	