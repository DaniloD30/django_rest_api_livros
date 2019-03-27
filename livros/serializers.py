from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Livro

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LivrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ('id', 'codigo', 'ISBN', 'titulo', 'autor', 'ano', 'editora')


