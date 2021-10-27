from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.decorators import api_view,authentication_classes,permission_classes 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,AllowAny


# Create your views here.

#authentications,permissions check chesetappudu  new chrome ni yeppatikappudu vaduthu undali(ctrl+shift+N)

@api_view(['GET','POST','PUT','PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
#@permission_classes([IsAuthenticated])
@permission_classes([IsAdminUser])
#@permission_classes([IsAuthenticatedOrReadOnly])
#@permission_classes([DjangoModelPermissions])
#@permission_classes([DjangoModelPermissionsOrAnonReadOnly])
#@permission_classes([AllowAny])
def student_api(request,pk=None):
	if request.method == "GET":
		id=pk
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer=StudentSerializer(stu)
			return Response(serializer.data)

		stu=Student.objects.all()
		serializer = StudentSerializer(stu,many=True)
		return Response(serializer.data)

	if request.method == "POST":
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	

	if request.method == "PUT":
		id=pk
		stu = Student.objects.get(pk=id)
		#serializer = StudentSerializer(instance=stu,data=request.data)
		#(OR)
		serializer = StudentSerializer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Complete Data Updated'})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

	if request.method == 'PATCH':
		id=pk
		stu = Student.objects.get(pk=id)
		serializer = StudentSerializer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partial Data Updated'})
		return Response(serializer.errors)
									

	
	if request.method == 'DELETE':
		id=pk
		stu=Student.objects.get(pk=id)
		stu.delete()
		return Response({'msg':'Data Deleted'})	