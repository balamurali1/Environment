from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import JackRateThrottle

# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=StudentSerializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]
	throttle_classes = [AnonRateThrottle,UserRateThrottle]
	#throttle_classes =[JackRateThrottle]



"""
settings.py lo last lo chudu timing ni set cheshanu..

AnonRateThrottle ante--> anon ani set cheshanu..
UserRateThrottle ante ---> user ani set cheshanu..
JackRateThrottle ante ----> jack ani set cheshanu..
"""		