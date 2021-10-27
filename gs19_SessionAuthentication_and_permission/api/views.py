from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
	queryset = Student.objects.all() #this is queryset
	serializer_class=Studentserializer #queryset ni JSON format lo ki conver chesthundi serializers.py file.. 
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated] #idi credentials(username/password) matrame aduguthundi,anthey kakunda idi staff lo tick mark unna vallani kuda allow chesthundi..
	#permission_classes = [AllowAny] #idi credential lekunna andarini allow chesthundi..
	#permission_classes = [IsAdminUser] #idi admin site lo "staff lo tick mark" unna vallani matrame allow chesthundi,superuser ni kuda allow chesthundi...
	#permission_classes = [IsAuthenticatedOrReadOnly]#idi pedithey credentials unte anni CURD operations cheyavachunu,credentials lekunte only read cheyavachunu ani artham.	
	#permission_classes = [DjangoModelPermissions]#credentials undali malli vachesi haa person ki permissions yemi euvvalo  admin.site lo actions euvali..
	#permission_classes = [DjangoModelPermissionsOrAnonReadOnly]#idi echinappudu "DjangoModelpermissions" admin.site lo euvanappudu only "Readonly work auvthundi".,admin.site lo "Djangomodelpermissions" echinappudu readonly work authundi DjangoModelpermissions lo echina actions kuda work auvthai..



"""

pratisari new chrome ni use chesthu check cheyali(ctrl+shift+N) 
"""


