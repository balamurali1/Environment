from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
	page_size=3
	ordering = 'name' #ela esthe name anni ordering lo vasthai..Alphabrtical order lo
	"""Cannot resolve keyword 'created' into field. Choices are: id, name, roll-->ee error vachinappudu
	ordering='name' ani pettu..
	"""
	cursor_query_param = 'cu' #url tag lo observer cheai ? mark pakkana..