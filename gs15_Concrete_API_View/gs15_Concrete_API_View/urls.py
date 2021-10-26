"""gs15_Concrete_API_View URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
	#concreate API Views---> combinations
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentListCreate.as_view()),
    path('studentreup/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    path('studentrede/<int:pk>/',views.StudentRetrieveDestroy.as_view()),
    path('studentreupde/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),

]	





"""
urlpatterns = [
	#concreate API Views --->singles URLS

    path('admin/', admin.site.urls),    
    path('studentapi/',views.StudentList.as_view()),
    path('studentadd/',views.StudentCreate.as_view()),
    path('studentret/<int:pk>/',views.StudentRetrieve.as_view()),
    path('studentupdate/<int:pk>/',views.StudentUpdate.as_view()),
    path('studentdelete/<int:pk>/',views.StudentDelete.as_view()),
    
]
"""


