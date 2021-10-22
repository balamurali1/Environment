from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
#(OR)
#from rest_framework.mixins import *			


# Create your views here.

class Studentlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
	queryset = Student.objects.all() # This is queryset
	serializer_class = StudentSerializer  #This is serializers
	def get(self,request): #request anedi by default ga get() ni esthundi
		return self.list(request)

	def post(self,request): 
		return self.create(request)	


class Studentall(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
	queryset = Student.objects.all() # This is queryset
	serializer_class = StudentSerializer  #This is serializers
	def get(self,request,**kwargs): #request anedi by default ga get() ni esthundi
		return self.retrieve(request,**kwargs)

	def put(self,request,**kwargs): 
		return self.update(request,**kwargs)

	def delete(self,request,**kwargs): 
		return self.destroy(request,**kwargs)
		
	