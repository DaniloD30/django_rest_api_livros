# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Livro
from livros.serializers import LivrosSerializer, UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer