from rest_framework import serializers
from Book.models import *

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = BooksModel
		fields = "__all__"

"""
serializers.py ni views.py lo rasukovali..
"""
