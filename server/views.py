import collections

from django.core.management.color import no_style
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from requests_html import HTMLSession, HTMLResponse
import requests

from server.models import Course
from server.serializers import CourseSerializer


def parse_course_list(request):
	if not request.user.is_authenticated():
		return HttpResponse("Not authenticated.")
	session = HTMLSession()
	course_list_r = session.request(url='https://ocw.mit.edu/courses/', method='get')
	courses = course_list_r.html.find('.course_title')
	# Clear out old courses
	Course.objects.all().delete()
	sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Course])
	with connection.cursor() as cursor:
		for sql in sequence_sql:
			cursor.execute(sql)
	for course in courses:
		course_db_obj = Course(url=course.absolute_links.pop())
		course_db_obj.save()

	return HttpResponse("Successfully added all ")


def parse_all_courses_view(request):
	if not request.user.is_authenticated():
		return HttpResponse("Not authenticated.")
	if Course.objects.count() == 0:
		return HttpResponse("No Courses in database.")
	# parse_courses().delay()
	return render(request, 'parsing_progress.html', {'course_count': Course.objects.count()})


def get_course(request, course_id):
	if request.method == 'GET':
		try:
			course = Course.objects.get(pk=course_id)
		except Course.DoesNotExist:
			return HttpResponse(status=404)
		serializer = CourseSerializer(course)
		return JsonResponse(serializer.data)


def index(request):
	return render(request, 'index.html')


def parse_course(request, course_id):
	try:
		course = Course.objects.get(pk=course_id)
	except Course.DoesNotExist:
		return HttpResponse("Bad Course Id")
	session = HTMLSession()
	info_r = session.request(url=course.url, method='get')
	# Deactivate bad courses
	if not info_r:
		course.active = False
		return HttpResponse("URL not valid.")
	# Make sure course is active
	course.active = True
	# Set course name
	course.name = info_r.html.find('#course_title', first=True).find()[0].text
	# Set course info
	course_info = info_r.html.find('#course_info', first=True)
	authors = course_info.find('[itemprop=author]', first=False)
	course.instructors = ""
	for i, author in enumerate(authors):
		if i != 0:
			course.instructors += ", "
		course.instructors += author.text
	for paragraph in course_info.find('p'):
		if 'itemprop' not in paragraph.attrs:
			course.course_num = paragraph.text
	course.asTaughtIn = course_info.find('[itemprop=startDate]', first=True).text
	course.level = course_info.find('[itemprop=typicalAgeRange]', first=True).text
	course.description = info_r.html.find('#description', first=True).find('p', first=True).text
	# Set course syllabus
	syllabus_r = session.request(url=course.url + '/syllabus/', method='get')
	if syllabus_r:
		syllabus = str(syllabus_r.html.find('#course_inner_section', first=True).html)
		# Removes help modals which come after the tag <!-- googleoff: index-->
		syllabus = syllabus[0:syllabus.index('<!--googleoff: index-->')]
		course.syllabus = syllabus
	else:
		course.syllabus = "N/A"
	# Set course readings
	readings_r = session.request(url=course.url + '/readings/', method='get')
	if readings_r:
		readings = str(readings_r.html.find('#course_inner_section', first=True).html)
		# Removes help modals which come after the tag <!-- googleoff: index-->
		readings = readings[0:readings.index('<!--googleoff: index-->')]
		course.readings = readings
	else:
		course.readings = "N/A"
	# Set course tools
	tools_r = session.request(url=course.url + '/tools/', method='get')
	if tools_r:
		tools = str(tools_r.html.find('#course_inner_section', first=True).html)
		# Removes help modals which come after the tag <!-- googleoff: index-->
		tools = tools[0:tools.index('<!--googleoff: index-->')]
		course.tools = tools
	else:
		course.tools = "N/A"
	# Save course
	course.save()
	return HttpResponse("Successfully parsed course " + str(course_id) + ".")
