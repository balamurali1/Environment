from rest_framework import serializers
from . models import *

class Studentserializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"

"""
first we will create serializer class and we will import inside model class
"""

'''
Note: serializers is convert to 'queryset' ni JSON/XML data lo ki change chesthundi..

queryset is nothing but database lo unde table lo ni row and columns lo unde data ni queryset antatu..
'''