from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class Studentviewset(viewsets.ViewSet):
	def list(self,request):  #list is nothing but GET()
		queryset = Student.objects.all() #this is queryset
		serializer = Studentserializer(queryset,many=True)#many=True,ante table(queryset) lo chala records untai kabbti, annitini serializers lo ki marchali kabbati many=True ani pettali
		return Response(serializer.data)


	"""
	#retrieve ante display() ani,Use GET()
	pk=None anedi prasthuthaniki matrame,yepudaithey id ni url lo pass chesthe appudu ikkada ku vasthundi EX:pk=5 ani ela internal ga vachi untundi]
	"""	
	def retrieve(self,request,pk=None):  
		id=pk #ex: ikkada  ela id=5 ani internal ga vasthundi
		if id is not None:  # True auvthundi..
			queryset = Student.objects.get(id=id) #ikkada left side unna id vachesi column name ani artham,right side unna id lo 5 store aiye untundi,id=5 ani vasthundi internal ga.
			serializer= Studentserializer(queryset)
			return Response(serializer.data)	
			'''
			None meaning ante empty ga undi ani artham,appudu Fasle vasthundi
			not None meaning ante empty ga ledu,andulo yedo value undi ani artham..appudu True vasthundi 
			'''

	
	def update(self,request,pk): #mundu ga GET() chesi modify chesi,put() use cheai,diniki patch work kavadam ledu
		id=pk
		queryset = Student.objects.get(pk=id)
		serializer = Studentserializer(queryset,data=request.data)
		if serializer.is_valid(): #serializer lo unde data valid aithey(correct aithey) True vasthundi
			serializer.save()	 #valid aina data ni save() chesuko ani artham
			return Response({"msg":"Complete data Updated"})
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	
	


	def destroy(self,request,pk): #use DELETE() 
		id=pk
		queryset= Student.objects.get(pk=id)
		queryset.delete()
		return Response({'msg':'Record is Deleted!'})

	
	def create(self,request):  #create is nothing but post()
		serializer=Studentserializer(data=request.data) #request.data dwara data ni serializer lo ki pampisthunnamu
		if serializer.is_valid(): #serializer lo unde data valid aithey True vachi save auvthundi,internal ga jaruguthundi
			serializer.save()
			return Response({'msg':'complete data Created'})
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)						