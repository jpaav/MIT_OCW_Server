from django.db import models


class CourseDiscipline(models.Model):
	objects = models.Manager()
	name = models.CharField(max_length=100, null=True, blank=True)
	parent = models.ForeignKey(
		'CourseDiscipline',
		null=True,
		blank=True
	)


class Course(models.Model):
	objects = models.Manager()
	name = models.CharField(max_length=500, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	active = models.BooleanField(blank=False, null=False, default=False)
	course_num = models.CharField(max_length=10, null=True, blank=True)
	instructors = models.CharField(max_length=500, null=True, blank=True)
	level = models.CharField(max_length=500, null=True, blank=True)
	asTaughtIn = models.CharField(max_length=500, null=True, blank=True)
	description = models.CharField(max_length=2000, null=True, blank=True)
	# html
	syllabus = models.CharField(max_length=20000, null=True, blank=True)
	# html
	readings = models.CharField(max_length=20000, null=True, blank=True)
	# html
	tools = models.CharField(max_length=20000, null=True, blank=True)
	discipline = models.ForeignKey(
		CourseDiscipline,
		null=True,
		blank=True
	)

