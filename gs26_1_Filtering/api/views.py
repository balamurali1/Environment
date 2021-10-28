from django.shortcuts import render
from . serializers import StudentSerializer
from . models import Student
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentList(ListAPIView):	
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	filter_backends = [DjangoFilterBackend] #filtering local lo set cheyadam ela...
	#filterset_fields = ['city']
	#filterset_fields = ['name','city']
	filterset_fields = ['id','city']



#filers ni global lo set cheshanu(settings.py lo last lo)
#first you will install, pip install django-filter	