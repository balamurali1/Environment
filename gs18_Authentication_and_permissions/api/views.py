from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=Studentserializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated] #idi credential aduguthundi,anthey kakunda idi staff lo tick mark unna vallani kuda allow chesthundi..
	#permission_classes = [AllowAny] #idi credential lekunna andarini allow chesthundi..
	#permission_classes = [IsAdminUser] #idi admin site lo "staff lo tick mark" unna vallani matrame allow chesthundi,superuser ni kuda allow chesthundi...


"""

pratisari new chrome ni use chesthu check cheyali(ctrl+shift+N) 
"""


