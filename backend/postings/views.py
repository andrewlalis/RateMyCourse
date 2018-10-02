from django.shortcuts import render
from django.http import HttpResponse
from postings.models import *

# Create your views here.

# The view for the homepage, or index.html
def index(request):
	return render(request, 'postings/index.html')

def universities(request):
	universities_list = University.objects.all()
	context = {'entities': universities_list}
	return render(request, 'postings/collections/universities.html', context)

def courses(request):
	courses_list = Course.objects.all()
	context = {'entities': courses_list}
	return render(request, 'postings/collections/courses.html', context)