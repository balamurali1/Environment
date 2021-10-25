from django.shortcuts import render
from rest_framework.response import Response
from . models import Student
from . serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView



# Create your views here.

# request ante, browser(EX:chrome) lo unde "url tag meeda hit cheyagane" request pass(send) auvthundi server ki internal ga..

class Student_api(APIView): #request is nothing but "server ki request send" cheyadam..
	def get(self, request, pk=None, format=None):
		id=pk
		if id is not None: #None ante empty ani artham, not None ante yedoo value undi ani artham...
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)

		stu=Student.objects.all()
		serializer = StudentSerializer(stu,many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = StudentSerializer(data=request.data) #request.data ante, "client code rasi" serializer lo ki pampisthunnadu ani artham..
		if serializer.is_valid(): #serializer lo unde data valid aithey save chesuko ani cheppadam...
			serializer.save()
			return Response({'msg':'Data Crated'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) #paina if conditions lo yemaina problem vachi serializer fail aithey appudu ee line execute auvthundi..
	

	def put(self, request, pk, format=None):
		id=pk
		stu = Student.objects.get(pk=id)
		serializer = StudentSerializer(instance=stu,data=request.data) #instance nothing but "perticular id lo unde" old data stored in database again(after modifications)
		if serializer.is_valid():						               #put lo vachesi request.data ante, "client code modify chesi" serializer lo ki pampisthunnadu ani artham..
			serializer.save()
			return Response({'msg':'Complete Data Updated!!'})
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	

	def patch(self, request, pk, format=None):
		id=pk
		stu = Student.objects.get(pk=id)
		serializer = StudentSerializer(instance=stu, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'partial Data Updated'})
		return Response(serializer.errors) #ee line lo status by default ga vasthundi andukey rayaledu...
	

	def delete(self, request, pk, format=None):
		id = pk
		stu = Student.objects.get(pk=id)
		stu.delete()
		return Response({'msg':'Data Deleted'})		
