from django.urls import path
from Book.views import *

urlpatterns = [
	path('',Booklist),
	path('add/',post_Book),
	path('update/<int:id>/',update_Book),
	path('delete/<int:id>/',delete_Book),
]