from rest_framework import serializers
from postings.models import *



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

class ReviewHelpfulVoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReviewHelpfulVote
		fields = [
			'pk',
			'review',
			'helpful',
			'user'
		]
		read_only_fields = [
			'pk'
		]