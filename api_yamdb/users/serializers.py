from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('You can\'t use this username!')
        return value


class TokenObtainSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(max_length=150, write_only=True)
    username = serializers.CharField(max_length=150, write_only=True)


class UserManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'role',
                  'first_name',
                  'last_name',
                  'bio')
