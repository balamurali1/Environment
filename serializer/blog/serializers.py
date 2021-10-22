from rest_framework import serializers
from blog.models import Student


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields='__all__'




'''
queryset ante, data base lo  unde table lo ni data ni queryset antaru..
serializer anedi, queryset ni JOSN/XML format lo ki convert chesthundi...


serializer di main resion yemiti ante queryset(data base lo unde table lo ni data ni)  
JSON/XML format lo ki marchadame....
'''		