from django.contrib import admin
from Book.models import *

# Register your models here.

#admin.site.register(Student)

		#(OR)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display=('id','name','roll','city')		