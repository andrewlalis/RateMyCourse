from .views import *
from django.urls import path, re_path




urlpatterns = [
	# /api/postings/reviews/ Lists all review objects.
	path('reviews/', ReviewsView.as_view(), name='reviews'),
	# /api/postings/reviews/1/ Returns data for one Review.
	path('reviews/<int:pk>', ReviewView.as_view(), name='review'),

	# /api/postings/universities/ Lists all university objects.
	path('universities/', UniversitiesView.as_view(), name='universities'),
	# /api/postings/universities/1/ Returns data for one University.
	path('universities/<int:pk>', UniversityView.as_view(), name='university'),

	# /api/postings/courses/ Lists all course objects.
	path('courses/', CoursesView.as_view(), name='courses'),
	# /api/postings/courses/1/ Returns data for one Course.
	path('courses/<int:pk>', CourseView.as_view(), name='course'),

	# /api/postings/professors/ Lists all professor objects.
	path('professors/', ProfessorsView.as_view(), name='professors'),
	# /api/postings/professors/1/ Returns data for one Professor.
	path('professors/<int:pk>', ProfessorView.as_view(), name='professor'),
	
	# Deprecated
	re_path(r'^(?P<pk>\d+)/$', UniReviewRudView.as_view(), name='post-rud'),
	re_path(r'^$', UniReviewAPIView.as_view(), name='post-create')
]