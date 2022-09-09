from rest_framework import serializers

from .models import ROLE_CHOICES, User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(value):
        if value == 'me':
            raise serializers.ValidationError('You can\'t use this username!')


class TokenObtainSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class UserManageSerializer(serializers.ModelSerializer):
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

    def validate_username(value):
        if value == 'me':
            raise serializers.ValidationError('You can\'t use this username!')


class SelfUserSerializer(serializers.ModelSerializer):
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

    def validate_username(value):
        if value == 'me':
            raise serializers.ValidationError('You can\'t use this username!')
