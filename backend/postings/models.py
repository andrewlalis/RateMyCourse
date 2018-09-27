from django.db import models

# Represents any object for which reviews can be made. (Universities, Professors, etc.)
class RateableEntity(models.Model):
	# The human-readable name of this entity.
	name = models.CharField(max_length=256)

# A review represents any single data entry to the database.
class Review(models.Model):
	# An integer rating in the domain [1, 5]
	rating = models.IntegerField(default=1)
	# A title for the review (brief summary of sentiment)
	title = models.CharField(max_length=128)
	# The textual content of the review.
	content = models.TextField()
	# A foreign key referencing the entity for which this review was made.
	rateable_entity = models.ForeignKey('postings.RateableEntity', on_delete=models.CASCADE)
	# The date and time at which this review was published.
	created_date = models.DateTimeField(auto_now_add=True)
	# The date and time at which the last modification to this review was published.
	last_updated_date = models.DateTimeField(auto_now=True)

# A vote for a review as either positive or negative.
class ReviewHelpfulVote(models.Model):
	# A reference to the review that this vote is for.
	review = models.ForeignKey('postings.Review', on_delete=models.CASCADE)
	# Whether or not the referenced review was helpful.
	helpful = models.BooleanField()
	# TODO: Add a reference to the user who voted. The whole purpose of a separate vote object is to track who votes for what.

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
	rating = models.IntegerField(default=1)
	title = models.CharField(max_length=200)
	date_published = models.DateField('date published')
	content = models.CharField(max_length=200)
	