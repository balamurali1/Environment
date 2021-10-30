from enroll.models import User
from enroll.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]


#chrome lo data ravali ani  Global lo code rashanu adi  ..results kuda JSON format lone esthundi..	
