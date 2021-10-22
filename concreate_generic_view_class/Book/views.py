from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

# Create your views here.

######### ListAPIView ###########
class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer


######## CreateAPIView##########
class Studentcreate(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer


####### RetrieveAPIView ###########
class Studentretrieve(RetrieveAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

######### UpdateAPIView ############

class Studentupdate(UpdateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

######### DestroyAPIView ###########

class Studentdelete(DestroyAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer






