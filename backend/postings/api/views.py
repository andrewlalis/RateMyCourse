from rest_framework import generics, mixins
from postings.models import *
from .serializers import *
from django.db.models import Q
from django.http import *


# The view for listing all generic Review objects.
class ReviewsView(mixins.CreateModelMixin, generics.ListAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

# View for an individual Review object.
class ReviewView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

def review_helpful_vote(request, review_id):
	if request.method == 'POST':
		helpful = request.POST.get('helpful')
		if helpful is None:
			return HttpResponseBadRequest("Bad Request")
		helpful = True if helpful == 'true' else False

		try:
			review = Review.objects.get(pk=review_id)
		except Review.DoesNotExist:
			raise HttpResponseBadRequest("Bad Request: Invalid review id.")

		vote = ReviewHelpfulVote.objects.create(
			review=review,
			helpful=helpful
		)

		return HttpResponse(status=201)

	return HttpResponseBadRequest("Bad Request")