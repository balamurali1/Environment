from django.shortcuts import render
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
	def list(self,request):
		stu = Student.objects.all()
		serializer = StudentSerializer(stu,many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		id=pk
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer=StudentSerializer(stu)
			return Response(serializer.data)

	def create(self, request):
		serializer =StudentSerializer(data=request.data)#request.data ante 'client' rasina data ni seraializer lo ki pampisthunnamu ani artham...
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
	def update(self, request, pk): #put() method antaru...
		id=pk
		stu=Student.objects.get(pk=id)
		serializer =StudentSerializer(instance=stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data is Updated'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	
	def partial_update(self, request, pk): #Patch() method antaru...
		id=pk
		stu=Student.objects.get(pk=id)
		serializer =StudentSerializer(instance=stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'partial is Updated'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors) #ikkada status rayakapoinna patch lo by default ga code fail ainappudu status message vasthundi..		
		

	
	def destroy(self, request, pk):
		id=pk
		stu = Student.objects.get(pk=id)
		stu.delete()
		return Response({'msg':'Data Deleted'})	

