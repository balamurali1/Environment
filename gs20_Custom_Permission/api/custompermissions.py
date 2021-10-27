from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
	def has_permission(self, request, view): #ikkada request lo bydefault get() untundi..
		if request.method == "GET": #True auvthundi
			return True
		return False


"""
class MyPermission(BasePermission):
	def has_permission(self, request, view): #ikkada request lo bydefault get() untundi..
		if request.method == "POST": #False auvthundi
			return True
		return False
"""						

"""
Custompermissions ante manamu mana hands tho own ga rase danini Custompermissions antaru
"""
