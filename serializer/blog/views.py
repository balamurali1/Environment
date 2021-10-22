from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Student
from blog.serializers import StudentSerializer


# Create your views here.

@api_view(['GET'])  
def home(request):
	student_obj = Student.objects.all()  #student_obj(ante queryset ani artham)
	serializer = StudentSerializer(student_obj,many=True) #many=True,ante objects(records) ekkuva untai kabbati many=True ani pettali.
  
	return Response({'status':200,'payload':serializer.data}) 
	'''
	1.serializer.data ante query set ni serializers lo ki convert chesi na data kavali ani..(ante JSON/XML data kavali ani)

	2.serializer.data ante, serializer lo unde data(JSON/XML) ani artham
	'''


'''
@api_view(['POST'])
def post_student(request):
	data = request.data
	print(data)
	return Response({'status':200,'payload':data})

#Note: edi yenduku rashado naku artham kaledu,execute kuda cheyaledu..
'''