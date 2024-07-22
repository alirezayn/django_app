from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import UserToken
from .serializers import UserTokenSerilizer

class UserTokenViewSet(ModelViewSet):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerilizer
    