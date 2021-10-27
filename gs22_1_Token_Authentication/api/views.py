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
	

# okasari model.py file chudu.new user ni create cheyagane Token automatic ga create ayye vidhanga  signal topic use chesi code rashanu...