from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 3
	#limit_query_param = 'mylimit' #optional
	#offset_query_param = 'myoffset' #optional
	#max_limit= 6  #optional