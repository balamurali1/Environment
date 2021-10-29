from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
	page_size = 3 #ikkada number change chesthu chudu...
	#page_query_param = 'p' #optional 
	#page_size_query_param = 'records' #optional
	#max_page_size = 7 #optional
	