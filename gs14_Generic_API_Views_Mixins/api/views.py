"""
GenericAPIView and Model Mixin(idi use chesi code ni Function Based API Views,classes Based API Views
kanna esay ga rayavachunu..)
"""
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


"""
ListModelMixin anedi,.list() and get() function ni refer chesthundi..
"""
class StudentList(GenericAPIView,ListModelMixin):
	queryset = Student.objects.all() #queryset means database lo unde table data ni queryset antaru
	serializer_class=StudentSerializer #ee queryset ni serializer anedi JSON format lo ki change chesthundi..

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)


"""
CreateModelMixin anedi,.create() and post() function ni refer chesthundi..
"""
class StudentCreate(GenericAPIView,CreateModelMixin):
	queryset = Student.objects.all() #queryset means database lo unde table data ni queryset antaru
	serializer_class=StudentSerializer #ee queryset ni serializer anedi JSON format lo ki change chesthundi..

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


"""
RetrieveModelMixin is noting but "display" ani artham..
RetrieveModelMixin anedi, .retrieve() and get() function ni refer ni chesthundi..
RetrieveModelMixin is display the particular 'id' record  ni display chesthundi..
"""

class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
	queryset = Student.objects.all() 	
	serializer_class=StudentSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs) # internal ga  url.py lo menction chesina pk {'pk':3}, ee line lo ki vasthundi internal ga vachi .retrieve() method call auvthundi


"""
UpdateModelMixin anedi,put() and .update() functions ni refer chesthundi...
UpdateModelMixin is update particular record(object)

UpdateModelMixin anedi it will work both "put and Patch"
"""

class StudentUpdate(GenericAPIView,UpdateModelMixin):
	queryset = Student.objects.all() 	
	serializer_class=StudentSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs) # internal ga url.py lo menction chesina pk {'pk':3}, ee line lo ki vasthundi internal ga vachi .update() method call auvthundi


"""
DestoryModelMixin anedi delete() and .destroy() functions ni refer chesthundi... 
DestoryModelMixin is noting but delete() cheyadam ani..particular record(object)
"""

class StudentDestroy(GenericAPIView,DestroyModelMixin):
	queryset = Student.objects.all() 	
	serializer_class=StudentSerializer

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs) #internal ga url.py lo menction chesina pk {'pk':3}, ee line lo ki vasthundi internal ga vachi .update() method call auvthundi



