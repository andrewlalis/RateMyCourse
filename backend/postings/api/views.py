from rest_framework import generics, mixins
from postings.models import UniversityReview, Review
from .serializers import *
from django.db.models import Q


class UniReviewRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = UniversityReviewSerializer

	def get_queryset(self):
		return UniversityReview.objects.all()
class UniReviewAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = UniversityReviewSerializer

	def get_queryset(self):
		qs = UniversityReview.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
		return qs

	def post(self,request,*args,**kwargs):
		return self.create(request, *args, **kwargs)

# The view for listing all generic Review objects.
class ReviewsView(mixins.CreateModelMixin, generics.ListAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

# View for an individual Review object.
class ReviewView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

# The view for listing all Universities.
class UniversitiesView(generics.ListAPIView):
	serializer_class = UniversitySerializer
	queryset = University.objects.all()

# The view for an individual University.
class UniversityView(generics.RetrieveUpdateDestroyAPIView):
	queryset = University.objects.all()
	serializer_class = UniversitySerializer

# The view for listing all Courses.
class CoursesView(generics.ListAPIView):
	serializer_class = CourseSerializer
	queryset = Course.objects.all()

# The view for an individual Course.
class CourseView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

# The view for listing all Professors.
class ProfessorsView(generics.ListAPIView):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializer

# The view for an individual Professor.
class ProfessorView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializer