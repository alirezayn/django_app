from rest_framework import serializers 
from .models import UserToken

class UserTokenSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = UserToken
        fields = '__all__'