from rest_framework import generics, mixins
from postings.models import UniversityReview
from .serializers import UniversityReviewSerializer
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
