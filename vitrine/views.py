from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, CarroSerializer
from .models import Carro

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all().order_by('valor', '-id')
    serializer_class = CarroSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]