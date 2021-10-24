from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

#Model Object -->Single Student Data
"""
def student_detail(request,pk): #ikkada unna 'request' lo by default ga 'get' untundi..get anedi server ki pothundi okay..
	stu = Student.objects.get(id = pk)
"""

#(OR) Nenu just id,pk yela pani chesthayoo just chesk cheshanu. only function ni different different ga rasi chusha..anthey..


def student_detail(request,id): #ikkada unna 'request' lo by default ga 'get' untundi..get anedi server ki pothundi okay..	 
	stu = Student.objects.get(pk = id)
	"""
	Model Objects(record/object) ni thisukunna database tabel nundi Dinine "Complext data" antaru
	"""
	serializer = StudentSerializer(stu)
	"""
	Complext data nu serializer lo ki convert cheshanu,adi python dictionary(python data)/Serializing Queryset ga
	marindi..
	"""
	json_data = JSONRenderer().render(serializer.data)
	"""
	ee python data(python dictionary)/Serializing Queryset ni, "JSON/XML format" lo ki marcha daniki
	JSONRenderer() ni use cheshamu.. 
	"""
	return HttpResponse(json_data,content_type='application/json')
	"""
	json_data(JSON Format lo ki marina data ni) clients ki 'Froent-end' kanipinchadaniki
	HttpResponse() ni use cheshamu..

	content_type ante, application anedi json format lo ki marindi ani cheppadaniki..
	"""


#Query Set -All Student Data

def student_list(request): 	 
	stu = Student.objects.all()
	"""
	Model Objects(records/objects) ni thisukunna database tabel nundi Dinine "Complext data" antaru
	"""
	serializer = StudentSerializer(stu,many=True) 
	"""
	Complext data nu serializer lo ki convert cheshanu,adi python dictionary(python data)/Serializing Queryset ga
	marindi..

	many=True ante, Queryset(database lo chala records untai) kabbati avi anni kuda..
	python dictionary(python data)/Serializing Queryset ga marali ani artham..
	"""
	json_data = JSONRenderer().render(serializer.data)
	"""
	ee python data(python dictionary)/Serializing Queryset ni, "JSON/XML format" lo ki marcha daniki
	JSONRenderer() ni use cheshamu.. 
	"""
	return HttpResponse(json_data,content_type='application/json')
	"""
	json_data(JSON Format lo ki marina data ni) clients ki 'Froent-end' kanipinchadaniki
	HttpResponse() ni use cheshamu..

	content_type ante, application anedi json format lo ki marindi ani cheppadaniki..
	"""	





