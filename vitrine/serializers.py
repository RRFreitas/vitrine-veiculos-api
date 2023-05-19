from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Carro

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id', 'nome', 'marca', 'ano', 'km', 'estado', 'valor', 'foto']