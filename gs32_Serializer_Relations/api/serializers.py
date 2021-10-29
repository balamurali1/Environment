from api.models import Singer,Song
from rest_framework import serializers

class SingerSerializer(serializers.ModelSerializer):
	#song1 = serializers.StringRelatedField(many=True,read_only=True) #ela code rasi pedithy "record id kakunda" direct ga song name kuda kanipisthundi..API wrowser(chrome lo) lo,ee line comment petti chusthe only record id matrame kanipisthundi..
	#song1 = serializers.PrimaryKeyRelatedField(many=True,read_only=True) #ela rasthe only "records ids" kanipisthai...
	#song1 = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail') #(song-detali-->modeltable name-detail),ela rasthe "hyperlinkes" create chesi esthundi..	
	#song1 = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title') # title ante,song table lo unde title field ani artham..(idi kuda song names ni chupisthundi..)
	#song1 = serializers.SlugRelatedField(many=True,read_only=True,slug_field='duration') #ela rasthe song yooka duration chupisthundi...
	song1 = serializers.HyperlinkedIdentityField(view_name='song-detail') #song-list-->modeltable name-detail(idi okey oka hyperlink ni matrame esthundi..)
	class Meta:
		model = Singer
		fields = ['id','name','gender','song1']  
		"""
		 Singer table lo ki nenu Song table lo unde "ralated_name(song1)" anedi esthey,appudu singer
		 ane person vachesi yenni songs padinado,yevariki padinado haa "record id", singer table lo ne telusthundi...API wrowser(chrome lo) lo
		"""

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ['id','title','singer','duration']

