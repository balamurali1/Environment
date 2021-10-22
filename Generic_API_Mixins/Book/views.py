from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
#(OR)
#from rest_framework.mixins import *			


# Create your views here.
'''
GenericAPIView andedi by default ga class() lo euuvali

ListModelMixin anedi,.list() and get() function ni refer chesthundi..
'''
class Studentlist(GenericAPIView,ListModelMixin):
	queryset = Student.objects.all() # This is queryset
	serializer_class = StudentSerializer  #This is serializers
	def get(self,request): #request anedi by default ga get() ni esthundi
		return self.list(request)


"""
CreateModelMixin anedi , .create() and post() function ni refer chesthundi..
"""
class Studentcreate(GenericAPIView,CreateModelMixin):
	queryset = Student.objects.all() # This is queryset
	serializer_class = StudentSerializer  #This is serializers
	def post(self,request): #request anedi by default ga get() ni esthundi
		return self.create(request)
		


"""
RetrieveModelMixin is noting but "display" ani artham..

RetrieveModelMixin anedi, .retrieve() and get() function ni refer ni chesthundi..

RetrieveModelMixin is display the particular 'id' record  ni display chesthundi..
"""
class Studentdisplay(GenericAPIView,RetrieveModelMixin):
	queryset = Student.objects.all() # This is queryset
	serializer_class = StudentSerializer  #This is serializers
	def get(self,request,**kwargs): #request anedi by default ga get() ni esthundi
		return self.retrieve(request,**kwargs)


"""
UpdateModelMixin anedi,put() and .update() functions ni refer chesthundi...

UpdateModelMixin is update particular record(object)
"""

class Studentupdate(GenericAPIView,UpdateModelMixin):
	queryset = Student.objects.all() # This is queryset
	serializer_class = StudentSerializer  #This is serializers
	def put(self,request,**kwargs): #request anedi by default ga get() ni esthundi
		return self.update(request,**kwargs)



"""
DestoryModelMixin anedi delete() and .destroy() functions ni refer chesthundi... 

DestoryModelMixin is noting but delete() cheyadam ani..particular record(object)
"""
class Studentdelete(GenericAPIView,DestroyModelMixin):
	queryset = Student.objects.all() # This is queryset
	serializer_class = StudentSerializer  #This is serializers
	def delete(self,request,**kwargs): #request anedi by default ga get() ni esthundi
		return self.destroy(request,**kwargs)










		