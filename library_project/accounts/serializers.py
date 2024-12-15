from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    """"
    A serializer for creating user instances in the Library Management API
    """
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'}, #makes the password input for the Browsable API hidden
    ) 

    class Meta:
        model = get_user_model()
        fields = ['password','username', 'email']

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user
    
class ProfileInfoSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    email = serializers.EmailField(required=False)
    class Meta:
        model = get_user_model()
        fields = ['username','bio','email']
