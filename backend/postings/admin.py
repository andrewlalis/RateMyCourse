from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(UniversityReview)
admin.site.register(Review)
admin.site.register(RateableEntity)
admin.site.register(ReviewHelpfulVote)
admin.site.register(University)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(User)