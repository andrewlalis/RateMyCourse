from .views import UniReviewRudView,UniReviewAPIView
from django.urls import re_path




urlpatterns = [

	re_path(r'^(?P<pk>\d+)/$', UniReviewRudView.as_view(), name='post-rud'),
	re_path(r'^$', UniReviewAPIView.as_view(), name='post-create')
]