from django.shortcuts import render
from Book.models import *
from Book.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

##################### read #################
@api_view(['GET'])
def Booklist(request):  #function lo by default ga 'request' untundi..okay..
	booksobj = BooksModel.objects.all() #This is queryset
	serializer = BookSerializer(booksobj,many=True) #many=True,ante objects(records) ekkuva untai kabbati many=True ani pettali.
	return Response(serializer.data) #serializer.data ni manamu 'return Response' ga thisukunnamu..
	"""
	serializer.data(sapparet ga idi oka variable ani artham geekyshows lo chepinadu..) ante, 
	serializer lo unde data(JSON/XML) clients ki "Front end" kanapadali ante serialize.data(variable ni)use chesthamu ani artham..

	response means nothing but clients ki "Front end" kanipinchede response antaru..
	dinine HTTPResponse ani kuda antaru..
	"""

##################### create ################

@api_view(['POST'])
def post_Book(request):  #function lo by default ga 'request' untundi..okay..
	booksobj = BooksModel.objects.all() #This is queryset
	serializer = BookSerializer(data=request.data) #data ni post(create) cheyali kabbati "request.data" ani pettali
	if serializer.is_valid():
		serializer.save()		
	return Response(serializer.data) 



################# update(update ki kuda 'POST' use chesthamu) ##########
@api_view(['POST'])
def update_Book(request,id):  #function lo by default ga 'request' untundi..okay..
	booksobj = BooksModel.objects.get(pk=id) #This is queryset
	serializer = BookSerializer(instance=booksobj,data=request.data) #data ni post cheyali kabbati "request.data" ani pettali
	if serializer.is_valid():
		serializer.save()		
	return Response(serializer.data) 

'''
instance ante (object) ani artham	
'''
################### Delete #################

@api_view(['DELETE'])
def delete_Book(request,id):  #function lo by default ga 'request' untundi..okay..
	booksobj = BooksModel.objects.get(pk=id) #This is queryset
	booksobj.delete()
	return Response("Record is Deleted!!") 
