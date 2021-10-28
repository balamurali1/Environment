from api.models import  Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle


class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	throttle_scope = 'readstudentAPI' #peru yedaina rasuko.. ni estam,Dinini setting.py lo last lo timings set cheshanu chudu..

class StudentCreate(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	throttle_scope = 'modifystu'


class StudentRetrieve(RetrieveAPIView):#display, concreate API view lo auomatic ga pk ni internal thisukuntai..
	queryset = Student.objects.all()
	serializer_class=StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	throttle_scope = 'readstudentAPI' #peru yedaina rasuko.. ni estam,Dinini setting.py lo last lo timings set cheshanu chudu..

class StudentUpdate(UpdateAPIView):#concreate API view lo auomatic ga pk ni internal thisukuntai..
	queryset = Student.objects.all()
	serializer_class=StudentSerializer
	throttle_classes = [ScopedRateThrottle]	
	throttle_scope = 'modifystu'				
	
class StudentDelete(DestroyAPIView):#concreate API view lo auomatic ga pk ni internal thisukuntai..
	queryset = Student.objects.all()
	serializer_class=StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	throttle_scope = 'modifystu'