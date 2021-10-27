from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission


# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=Studentserializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	authentication_classes = [SessionAuthentication]
	permission_classes = [MyPermission] #idi credentials(username/password) matrame aduguthundi,anthey kakunda idi staff lo tick mark unna vallani kuda allow chesthundi..
	


"""

pratisari new chrome ni use chesthu check cheyali(ctrl+shift+N) 
"""


