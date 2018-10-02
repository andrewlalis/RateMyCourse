from django.db import models

# Represents an authenticated reviewer or reader of reviews.
class User(models.Model):
	# A non-unique name for the user.
	name = models.CharField(max_length=64)
	# The user's birth date.
	birth_date = models.DateField()

# Represents any object for which reviews can be made. (Universities, Professors, etc.)
class RateableEntity(models.Model):
	# Constants defined for types of rateable entities.
	UNIVERSITY = 0
	COURSE = 1
	PROFESSOR = 2
	TYPE_CHOICES = (
		(UNIVERSITY, 'University'),
		(COURSE, 'Course'),
		(PROFESSOR, 'Professor')
	)

	# The human-readable name of this entity.
	name = models.CharField(max_length=256)
	# The date and time at which this entity was created.
	created_date = models.DateTimeField(auto_now_add=True)
	# The type of entity this is.
	entity_type = models.SmallIntegerField(choices=TYPE_CHOICES)

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
	# A reference to the person who created this review.
	author = models.ForeignKey('postings.User', on_delete=models.PROTECT)

# A vote for a review as either positive or negative.
class ReviewHelpfulVote(models.Model):
	# A reference to the review that this vote is for.
	review = models.ForeignKey('postings.Review', on_delete=models.CASCADE)
	# Whether or not the referenced review was helpful.
	helpful = models.BooleanField()
	# TODO: Add a reference to the user who voted. The whole purpose of a separate vote object is to track who votes for what.

# A RateableEntity for universities.
class University(RateableEntity):
	# A string referring to the URL of the university. Every single university should have one.
	website_url = models.URLField()
	# A string referring to the location of the university.
	location = models.CharField(max_length=256)

# A RateableEntity for professors, who belong to one or more university.
class Professor(RateableEntity):
	# The universities that this professor teaches or has taught at.
	universities = models.ManyToManyField('postings.University')

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
	date_published = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=200)
	