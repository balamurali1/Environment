from django.contrib import admin
from Book.models import BooksModel

# Register your models here.

'''
admin.site.register(BooksModel)
'''
	#(OR)

@admin.register(BooksModel)
class BooksModelAdmin(admin.ModelAdmin):
	list_display = ['id','name','author','read_by']