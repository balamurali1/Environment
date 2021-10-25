from rest_framework import serializers
from . models import Student


#validators(first Priority)

def start_with_r(value): #geekyshows lo chusha nu.. video name validation(30:00) 
	if value[0].lower() != 'r':
		raise serializers.ValidationError('Name should be start with R')

"""
class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"
"""
#(OR)

class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=50, validators=[start_with_r])
	roll = serializers.IntegerField()
	city = serializers.CharField(max_length=50)
	


#(Second Priority)
#Custom "Field level" Validations(Geekyshows lo anthanu rasi na code veru nenu rasina code veru kani vailidations matramu antani rasina vidhanam batti rashanu..)

	def validate_roll(self,value):
		if value >= 105:
			raise serializers.ValidationError("Set Full")
		return value




#(Third Priority)
#Object Level Validations

	#Diniki post() method use cheai..
	def validate(self,data):  #ela (True and False=False)code rasinappudu matrame (third Priority) pani cheyadam ledu..
		nm = data.get('name')
		ct = data.get('city')

		if nm.lower() == 'rohit' and ct.lower() != 'ranchi': 
			raise serializers.ValidationError('City Must be RANCHI ')
		return data
		"""
		#True and False=False (data create auvthundi database lo okay na..)
		    {
        		"id": 11,
        		"name": "rohit",
        		"roll": 111,
        		"city": "ranchi"
    		}
		"""


	# def validate(self,data): #ela (True and True=True)code rasinappudu matrame (third Priority) pani chesthundi
	# 	nm = data.get('name')
	# 	ct = data.get('city')
															 
	# 	if nm.lower() == 'rohit' and ct.lower() != 'ranchi': 
	# 		raise serializers.ValidationError('City Must be RANCHI ')
	# 	return data		

		"""
		#True and True=True  (data create kadu database lo okay na..,Error Chupisthundi..)
		
			#post(create) chesetappudu postman lo "Hyd" capital lo esthey niku error artham auvthundi..
		    {
        		"id": 11,
        		"name": "rohit", #Ikkada rasthunna vati adharangane get() method thisukuntundi
        		"roll": 111,
        		"city": "Hyd"
    		}

    	atually if conditions lo undevi ani true aithey ne if lo unde statement execute auvthundi..	
		"""

