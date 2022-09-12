from rest_framework import serializers

from .models import ROLE_CHOICES, User


class ValidatedSerializer(serializers.ModelSerializer):
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('You can\'t use this username!')
        return value


class SignupSerializer(ValidatedSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class TokenObtainSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(max_length=150, write_only=True)
    username = serializers.CharField(max_length=150, write_only=True)


class UserManageSerializer(ValidatedSerializer):
    role = serializers.ChoiceField(choices=ROLE_CHOICES)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'role',
                  'first_name',
                  'last_name',
                  'bio')


class SelfUserSerializer(ValidatedSerializer):
    role = serializers.ChoiceField(choices=ROLE_CHOICES, read_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'role',
                  'first_name',
                  'last_name',
                  'bio')
