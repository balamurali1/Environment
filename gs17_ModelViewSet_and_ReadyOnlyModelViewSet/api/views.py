from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.


class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer


#ModelViewSet, idi use chesi CRUD operations cheyavachunu.... very very short cut code...	
