from django.urls import path
from Book import views

urlpatterns = [
	path('studentapi/',views.student_api),
    path('studentapi/<int:pk>/',views.student_api)

	
]