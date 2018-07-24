"""MIT_OCW_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, viewsets, serializers

from server import views

# Serializers define the API representation.
from server.models import Course

urlpatterns = [
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^admin/', admin.site.urls),
	# Parsing views, requires authentication
	url(r'^parse_all_courses/$', views.parse_all_courses, name="parse_all_courses"),
	url(r'^parse_course_list/$', views.parse_course_list, name="parse_course_list"),
	# Data reading views using REST, not authentication required
	url(r'^get_course/(?P<course_id>[0-9]+)/$', views.get_course, name="get_course"),

]
