"""RateMyCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path,path,include
from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView
from postings import views

urlpatterns = [
    # / routes to index.html
    path('', views.index, name='homepage'),

    # /universities routes to a list of universities.
    path('universities', views.universities, name='universities_list'),

    # /universities/<pk> routes to a specific university.
    path('universities/<int:university_id>', views.university_entity, name='university entity'),

    # /courses routes to a list of courses.
    path('courses', views.courses, name='courses_list'),

    # /courses/<pk> routes to a specific course.
    path('courses/<int:course_id>', views.course_entity, name='course entity'),

    # static files (*.css, *.js, *.jpg etc.) served on /
    # (assuming Django uses /static/ and /media/ for static/media urls)
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)),

    # /universities/1/ Shows the page for a university.
    # TODO: add pages for each rateable entity.
    path('admin/', admin.site.urls),
    re_path(r'^api/postings/', include(('postings.api.urls','postings'), namespace='api-postings')),
]
