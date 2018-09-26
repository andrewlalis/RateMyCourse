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

urlpatterns = [
    # / routes to index2.html
    url(r'^$', serve, kwargs={'path': 'index2.html'}),

    # static files (*.css, *.js, *.jpg etc.) served on /
    # (assuming Django uses /static/ and /media/ for static/media urls)
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)),

    # /universities/1/ Shows the page for a university.
    # TODO: add pages for each rateable entity.
    path('admin/', admin.site.urls),
    re_path(r'^api/postings/', include(('postings.api.urls','postings'), namespace='api-postings')),
]
