from rest_framework import serializers
from . models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"


#Custom Validations	
	def validate(self, data): #post,update chesthe error ravali ani condition echa..
		if data['roll'] < 101:
			raise serializers.ValidationError({'error':"roll cannot be less than 101"})	

		
		if data['name']: #post,update chesthe error ravali ani condition echa...
			for n in data['name']:
				if n.isdigit():
					raise serializers.ValidationError({'error':"name cannot be numeric"})

		return data	
			