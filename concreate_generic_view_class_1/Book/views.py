from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
#(OR)
#from rest_framework.generics import *

# Create your views here.

		#Combinations of "APIs"  Process

########## ListCreateAPIView-->GET(),POST() ############ here list(GET()) give all the records from database..
class StudentListCreate(ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer


########## RetrieveUpdateAPIView-->GET(),Put() and Patch() ############
class Studentretriveupdate(RetrieveUpdateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

########## RetrieveDestroyAPIView ---> GET(),DELETE() #############
class Studentretrivedelete(RetrieveDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

######### RetrieveUpdateDestroyAPIView-->GET(),PUT()and PATCH(),DELETE()#############

class Studentretriveupdatedelete(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer



