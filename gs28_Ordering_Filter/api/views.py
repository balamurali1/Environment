from django.shortcuts import render
from . serializers import StudentSerializer
from . models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter	
from rest_framework.filters import OrderingFilter

# Create your views here.

class StudentList(ListAPIView):	
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	filter_backends = [OrderingFilter]

# Filter meeda click chesthe ani options kanipisthai...	 
	