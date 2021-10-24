from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET','POST'])
def student_api(request): #function lo by default ga 'request' untundi.haa request lo get untundi internal ga..
	if(request.method == "GET"):
		stu = Student.objects.all() #This is queryset(table lo unde records ani artham)
		serializer = StudentSerializer(stu,many=True)
		"""
		stu(queryset)ni serializers lo ki esthe haa serializer vachesi queryset ni
		JSON format lo ki marusthundi.many=True ante queryset lo chala records untai
		kada annitini JSON format lo ki convert cheai ani artham..
		"""
		return Response(serializer.data) #serializer.data ante idi oka variable anta"geekyshows" lo chepinadu..
	if(request.method == "POST"):
		data = request.data
		serializer = StudentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			res = {'msg':'Data has been created Successfully'}
			return Response(res)
		return Response({'mag':serializer.errors}) #serializer.errors:-data create kakunte error emi vasthundo chupisthundi..ela esthe.	
