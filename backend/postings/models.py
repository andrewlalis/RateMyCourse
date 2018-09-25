from django.db import models

# Represents any object for which reviews can be made. (Universities, Professors, etc.)
class RateableEntity(models.Model):
	# The human-readable name of this entity.
	name = models.CharField(max_length=256)

# A review represents any single data entry to the database.
class Review(models.Model):
	# An integer rating in the domain [1, 5]
	rating = models.IntegerField(default=1)
	# The textual content of the review.
	content = models.TextField()
	# An integer representing the number of times a user found this review helpful.
	helpful_vote_count = models.IntegerField(default=1)
	# An integer representing the number of times a user found this review unhelpful.
	unhelpful_vote_count = models.IntegerField(default=1)
	# A foreign key referencing the entity for which this review was made.
	rateable_entity_id = models.ForeignKey('postings.RateableEntity', on_delete=models.CASCADE)

# A RateableEntity for universities.
class University(RateableEntity):
	pass

# A RateableEntity for professors, who belong to one or more university.
class Professor(RateableEntity):
	# The universities that this professor teaches or has taught at.
	university = models.ManyToManyField('postings.University')

# A RateableEntity for courses, which belong to a university, and have one or more professors.
class Course(RateableEntity):
	# The university that this course belongs to.
	taught_at_university = models.ForeignKey('postings.University', on_delete=models.CASCADE)
	# A list of professors that teach this course.
	professors = models.ManyToManyField('postings.Professor')

# Create your models here.
class UniversityReview(models.Model):
	university_name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	date_published = models.DateTimeField('date published')
	content = models.CharField(max_length=200)
	