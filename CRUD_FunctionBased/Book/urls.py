from django.urls import path
from Book import views

urlpatterns = [
	path('student_api/',views.student_api,name='student'),

	
]