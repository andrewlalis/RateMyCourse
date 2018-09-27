from rest_framework import serializers
from postings.models import *


class UniversityReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = UniversityReview
		fields = [
			'pk',
			'university_name',
			'rating',
			'title',
			'username',
			'date_published',
			'content',
		]
		read_only_fields =[
			'pk'
		]

# Serializes the generic Review object.
class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = [
			'pk',
			'rating',
			'title',
			'content',
			'rateable_entity',
			'created_date',
			'last_updated_date'
		]
		read_only_fields = [
			'pk',
			'created_date',
			'rateable_entity'
		]

# Serializes Universities.
class UniversitySerializer(serializers.ModelSerializer):
	class Meta:
		model = University
		fields = [
			'pk',
			'name'
		]
		read_only_fields = [
			'pk'
		]

# Serializes Courses.
class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = [
			'pk',
			'name',
			'taught_at_university',
			'professors'
		]
		read_only_fields = [
			'pk'
		]

# Serializes Professors.
class ProfessorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Professor
		fields = [
			'pk',
			'name',
			'universities'
		]
		read_only_fields = [
			'pk'
		]
