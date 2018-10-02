from django.shortcuts import render
from django.http import HttpResponse, Http404
from postings.models import *

# Create your views here.

# The view for the homepage, or index.html
# There is an optional 'search_query GET parameter, which, if provided, gives the template a 'results' variable.
def index(request):
	search_query = request.GET.get('search_query', None)
	results = None
	if search_query:
		results = RateableEntity.objects.filter(name__icontains=search_query)

	return render(request, 'postings/index.html', {'results': results})

# The view for a listing of universities.
def universities(request):
	universities_list = University.objects.all()
	context = {'entities': universities_list}
	return render(request, 'postings/collections/universities.html', context)

# The view for /universities/<pk> Displays one university entity.
def university_entity(request, university_id):
	try:
		university = University.objects.get(pk=university_id)
	except University.DoesNotExist:
		raise Http404("University does not exist")
	return render(request, 'postings/entity_pages/university.html', {'entity': university})

# The view for a listing of courses.
def courses(request):
	courses_list = Course.objects.all()
	context = {'entities': courses_list}
	return render(request, 'postings/collections/courses.html', context)

# The view for a specific course entity.
def course_entity(request, course_id):
	try:
		course = Course.objects.get(pk=course_id)
	except Course.DoesNotExist:
		raise Http404("Course does not exist")
	return render(request, 'postings/entity_pages/course.html', {'entity': course})