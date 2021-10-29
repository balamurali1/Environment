from . models import Singer,Song
from rest_framework import serializers



class SongSerializer(serializers.ModelSerializer): # idi painane undali ee class ,lekunte error vasthundi.
	class Meta:
		model = Song
		fields = ['id','title','singer','duration']


class SingerSerializer(serializers.ModelSerializer): #ee class  kinda ne undali,lekunte error vasthundi.
	song1 = SongSerializer(many=True,read_only=True) #song1 ante,related_name models.py lo chudu adi ikkada echanu..
	class Meta:
		model = Singer
		fields = ['id','name','gender','song1']			



	

