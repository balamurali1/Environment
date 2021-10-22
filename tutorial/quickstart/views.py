from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

'''
@api_view(['GET'])  
def home(request):
  return Response({'status':200,"message":"This is rest framework project"})
'''
'''
@api_view(['POST'])  
def home(request):
  return Response({'status':200,"message":"This is rest framework"})
'''

@api_view(['GET','POST'])  
def home(request):
  return Response({'status':200,"message":"This is Django Rest frame work..okay.."})
