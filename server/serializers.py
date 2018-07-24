from rest_framework import serializers
from server.models import Course


# class CourseSerializer(serializers.Serializer):
# 	name = serializers.CharField(read_only=True, max_length=500)
# 	url = serializers.URLField(read_only=True)
# 	active = serializers.BooleanField(read_only=True)
# 	course_num = serializers.CharField(max_length=10, read_only=True)
# 	instructors = serializers.CharField(max_length=500, read_only=True)
# 	level = serializers.CharField(max_length=500, read_only=True)
# 	asTaughtIn = serializers.CharField(max_length=500, read_only=True)
# 	description = serializers.CharField(max_length=2000, read_only=True)
# 	# html
# 	syllabus = serializers.CharField(max_length=20000, read_only=True)
# 	# html
# 	readings = serializers.CharField(max_length=20000, read_only=True)
# 	# html
# 	tools = serializers.CharField(max_length=20000, read_only=True)


class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = (
			'pk', 'name', 'url', 'active', 'course_num', 'instructors', 'level', 'asTaughtIn', 'description', 'syllabus',
			'readings', 'tools')
