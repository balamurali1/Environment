from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=Studentserializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	authentication_classes = [SessionAuthentication]
	#permission_classes = [IsAuthenticated]
	permission_classes = [IsAdminUser] 
	"""
	IsAdminUser anedi permission evariki esthundi ante cmd lo 'createsuperuser' lo user ni create 
	chesthamu chudu variki esthundi,virine superuser antaru...virine Admin antaru.
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