from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets


# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=Studentserializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	
"""
Global lo (sttring.py lost lo rashanu..) rasthe authentication,permissions, views.py lo rase prathi
class ki Global lo  unde authentication,permissions apply auvthai..
"""

"""
ModelViewSet lo ne anni APIs actions untai... it is  short cut code..

APIs actions means like .list()-->GET(),
.crate()-->POST(),
.update()-->first GET() chesi modify chesi malli send chesetappudu PUT()and PATCH() vadu..,
.retrieve()-->GET(),retrieve means display particular record(indtance)(objects),
.destroy()-->DELETE() 
	evi anni kuda ModelViewSet lo ne untai..
"""
