from django.shortcuts import render
from . serializers import StudentSerializer
from . models import Student
from rest_framework.generics import ListAPIView

# Create your views here.

class StudentList(ListAPIView):
	"""
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	"""

	"""
	queryset = Student.objects.filter(passby='user1')
	serializer_class = StudentSerializer
	"""

	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	def get_queryset(self):
		user = self.request.user #request lo get() bydefault ga untundi..
		return Student.objects.filter(passby=user)