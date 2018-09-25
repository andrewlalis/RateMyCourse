from rest_framework import serializers
from postings.models import UniversityReview


class UniversityReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = UniversityReview
		fields = [
			'pk',
			'university_name',
			'title',
			'username',
			'date_published',
			'content',
		]
		read_only_fields =[
			'pk',
			'username'
		]