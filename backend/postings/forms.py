from django import forms

# The form for creating a review for any sort of rateable entity.
class EntityReviewForm(forms.Form):
	# The integer rating from 1 to 5.
	rating = forms.IntegerField(min_value=1, max_value=5)
	# The title of the review.
	title = forms.CharField(max_length=128)
	# The textual content of the review.
	content = forms.CharField(widget=forms.Textarea)
	# The id of the entity for which the review is created.
	entity_id = forms.IntegerField()