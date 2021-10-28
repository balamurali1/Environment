from django.shortcuts import render
from . serializers import StudentSerializer
from . models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter	

# Create your views here.

class StudentList(ListAPIView):	
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	filter_backends = [SearchFilter]
	search_fields = ['city']
	#search_fields = ['city','passby']
	#search_fields = ['name']
	#search_fields = ['^name']
	#search_fields = ['=name'] #search lo rase name database lo unde name same(matchkavali)undali


#first you will install, pip install django-filter==2.4.0

# search(basename) ane name ni change cheyali ante.. setting.py lo last lo chudu rashanu code.. marindo ledo chudali ante urltag lo observer cheai....	