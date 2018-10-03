from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseRedirect
from postings.models import *
from postings.forms import *

# Create your views here.

# The view for the homepage, or index.html
# There is an optional 'search_query GET parameter, which, if provided, gives the template a 'results' variable.
def index(request):
	search_query = request.GET.get('search_query', None)
	results = None
	if search_query:
		# Filter objects based on case-insensitive contains filter.
		results = RateableEntity.objects.filter(name__icontains=search_query)

	return render(request, 'postings/index.html', {'results': results})

# The view for listing all rateable entities.
def rateables(request):
	entity_type = request.GET.get('type', None)
	entities = None
	if entity_type == "university":
		entities = University.objects.all()
	elif entity_type == "course":
		entities = Course.objects.all()
	else:
		entities = RateableEntity.objects.all()
	return render(request, "postings/rateables/entities.html", {'entities': entities})

# The view for any rateable entity.
def rateable_entity(request, entity_id):
	try:
		entity = RateableEntity.objects.get(pk=entity_id)

		# Try and get a more specific entity type from what is provided.
		if entity.entity_type == RateableEntity.UNIVERSITY:
			entity = University.objects.get(pk=entity.pk)
			template = "university.html"
		elif entity.entity_type == RateableEntity.COURSE:
			entity = Course.objects.get(pk=entity.pk)
			template = "course.html"

		# Set any auxiliary variables needed, like average rating.
		# This MUST be done after categorizing the object above.
		entity.average_rating = entity.getAverageRating()

	except RateableEntity.DoesNotExist:
		raise Http404("RateableEntity with id " + str(entity_id) + " does not exist.")
	return render(request, "postings/rateables/" + template, {'entity': entity})

# The view for receiving POST requests for new reviews.
def post_review(request):
	if request.method == 'POST':
		form = EntityReviewForm(request.POST)
		if form.is_valid():
			# Only if the request is a POST and the form is valid do we do anything.
			rating = form.cleaned_data['rating']
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			entity_id = form.cleaned_data['entity_id']
			try:
				entity = RateableEntity.objects.get(pk=entity_id)
			except RateableEntity.DoesNotExist:
				raise HttpResponseBadRequest("Bad Request: Invalid entity id.")

			# Creates the new Review object from the posted data.
			review = Review.objects.create(
				rating=rating,
				title=title,
				content=content,
				rateable_entity=entity
			)

			# Send the user back to the entity they were viewing.
			return HttpResponseRedirect('/rateables/' + str(entity_id))

	return HttpResponseBadRequest("Bad Request")