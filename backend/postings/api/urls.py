from .views import *
from django.urls import path, re_path




urlpatterns = [
	# /api/postings/reviews/ Lists all review objects.
	path('reviews/', ReviewsView.as_view(), name='reviews'),
	# /api/postings/reviews/1/ Returns data for one Review.
	path('reviews/<int:pk>', ReviewView.as_view(), name='review'),

	path('reviews/<int:review_id>/helpful_vote/', review_helpful_vote, name='review_helpful_vote'),
	
	# Deprecated
]