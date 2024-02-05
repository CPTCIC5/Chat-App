from rest_framework import serializers
from django.contrib.auth.models import User

#model serializers provide in built connectivity of the field like modelforms in forms of django,
# model seriaizers also
#cools

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_staff','is_active','is_superuser','date_joined','last_login']


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    """
    #thats why i said checking if password == confirm_password in the frontend itself is easier
    #yes and takes less memory, agreed.
    #2nd way for confirm_password
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    """
    def create(self, validated_data):
        #validated_data.pop('confirm_password', None)
        return User.objects.create_user(username=validated_data['username'],email=validated_data.get('email'),password=validated_data['password'])
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()