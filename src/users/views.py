from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from users.models import User,Team
from users.serializers import UserSerializer,TaskSerializer

# Create your views here.


    # user

class UserListCreateApi(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetailUpdateApi(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




    # Teams

class TeamsListCreateApi(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TaskSerializer
    

class TeamsDetailUpdateApi(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TaskSerializer
    
