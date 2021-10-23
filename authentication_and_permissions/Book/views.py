from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=Studentserializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


"""
prathi class ku  Atthencations,permissions esthu pothey code anedi peruguthu(incress)
auvthu pothundi..kada. ala incress kakunda undali ante "global lo authentication,permissions"euvvali(settings.py lo last ku)
ela global esthe views.py lo unde prati class ku,future lo rayaboyee class ku global lo unde
authentication,permissions apply auvthai okay na.... 

ee project vachesi authentication_and_permissions_1 lo rashanu haa project chudu..  
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