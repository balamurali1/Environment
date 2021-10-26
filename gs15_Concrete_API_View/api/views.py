from api.models import  Student
from api.serializers import StudentSerializer

"""
#concreate API Views---> Sigles
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
"""

#concreate API Views--->Combinations
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView



"""
#Concreate API Views--> Singles
class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

class StudentCreate(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer	

class StudentRetrieve(RetrieveAPIView):#concreate API view lo auomatic ga pk ni internal thisukuntai..
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

class StudentUpdate(UpdateAPIView):#concreate API view lo auomatic ga pk ni internal thisukuntai..
	queryset = Student.objects.all()
	serializer_class=StudentSerializer					

	
class StudentDelete(DestroyAPIView):#concreate API view lo auomatic ga pk ni internal thisukuntai..
	queryset = Student.objects.all()
	serializer_class=StudentSerializer

"""

#(OR)



#Concreat API Views---->Combinations

class StudentListCreate(ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer			


class StudentRetrieveUpdate(RetrieveUpdateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer				

	
class StudentRetrieveDestroy(RetrieveDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer	
	

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer	
