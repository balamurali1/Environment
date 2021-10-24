from rest_framework import serializers
from api.models import Student #idi serializers.ModelSerializer  ki sambandam vasthundi..

class StudentSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	name = serializers.CharField(max_length=100)
	roll = serializers.IntegerField()
	city = serializers.CharField(max_length=100)
"""
serializers.Serializer lo rasinappudu "id field" lekunte maname ela rasukovali..
"""	

#(OR)


# class StudentSerializer(serializers.ModelSerializer): 
# 	class Meta:
# 		model=Student
# 		fields="__all__"	

"""
serializers.ModelSerializer lo by default ga "id field" anedi untundi..internal ga okay na...
"""