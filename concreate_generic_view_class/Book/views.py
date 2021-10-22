from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

# Create your views here.

######### ListAPIView-->GET() ###########
class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer


######## CreateAPIView --> POST()##########
class Studentcreate(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer


####### RetrieveAPIView---> GET() ###########
class Studentretrieve(RetrieveAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

######### UpdateAPIView -->put() and patch() ############

class Studentupdate(UpdateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

######### DestroyAPIView---> delete() ###########

class Studentdelete(DestroyAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer






