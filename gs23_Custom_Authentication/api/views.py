from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import viewsets
from api.customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=StudentSerializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	authentication_classes = [CustomAuthentication]
	permission_classes = [IsAuthenticated]	