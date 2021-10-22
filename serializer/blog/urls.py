from django.urls import path
from blog.views import *

urlpatterns = [
	path('',home),
	#path('student/',post_student),
]