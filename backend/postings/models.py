from django.db import models

# Create your models here.
class UniversityReview(models.Model):
	university_name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	date_published = models.DateTimeField('date published')
	content = models.CharField(max_length=200)
	