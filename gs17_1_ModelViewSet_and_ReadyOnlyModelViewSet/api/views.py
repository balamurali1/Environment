from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer


#ReadOnlyModelViewSet, idi use chesthe only list()(list anedi ani records ni chupisthundi..),retrieve(display,particular record) matrame chudagalamu...	


