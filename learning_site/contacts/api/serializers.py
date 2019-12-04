from rest_framework import serializers
from ..models import profile
from django.contrib.auth.models import User

class user_serializer (serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta :
        model = User
        fields = ('username' ,'email',"password","password2")
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get("username"),email=validated_data.get("email")
        ,password=validated_data.get("password"))

class profile_serializer (serializers.ModelSerializer):
    user = user_serializer(required=False)
    class Meta:
        model = profile
        fields = ("user","degree")
    