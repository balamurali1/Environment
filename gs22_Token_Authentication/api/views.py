from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=StudentSerializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	

"""
Ee project lo Token create kavali ante database lo,cmd lo run chesetappudu ee command execute cheai..
			
			python.manage.py drf_create_token<username>
		EX: python.manage.py drf_create_token admin
		Ex: python.manage.py drf_create_token user1
		.........etc	
"""	
