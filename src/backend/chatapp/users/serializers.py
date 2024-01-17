from rest_framework import serializers
from django.contrib.auth.models import User

#model serializers provide in built connectivity of the field like modelforms in forms of django,
# model seriaizers also

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_staff','is_active','is_superuser','date_joined','last_login']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'],email=validated_data.get('email'),password=validated_data['password'])


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()