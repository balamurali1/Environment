from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		#fields = "__all__"
		#(OR)
		fields = ['id','name','roll','city']


"""
queryset ni serializers.py file lo rest_framework nundi import chesukunna "serializers" anedi
JSO
"""