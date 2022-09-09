from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .mixins import RetrieveUpdateViewSet
from .models import User
from .permissions import IsAdmin
from .serializers import (SelfUserSerializer, SignupSerializer,
                          TokenObtainSerializer, UserManageSerializer)
from .tokens import account_activation_token, get_tokens_for_user
from .utils import create_user


@api_view(['POST', ])
def sign_up(request):
    """Функция для создания учетной записи. Под конец отправляет письмо."""
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        create_user(serializer)
        return Response(request.data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def activate(request):
    """Функция для активации учетной записи и предоставления токена."""
    serializer = TokenObtainSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data['username']
        code = serializer.data['confirmation_code']
        try:
            user = User.objects.get(username=username)
            account_activation_token.check_token(user, code)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is None:
            return Response(
                'User not found',
                status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        token = get_tokens_for_user(user)
        return Response(token, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin, ]
    queryset = User.objects.all()
    serializer_class = UserManageSerializer

    def perform_create(self, serializer):
        create_user(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SelfUserViewset(RetrieveUpdateViewSet):
    serializer_class = SelfUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, ]

    def retrieve(self, request):
        user = get_object_or_404(self.queryset, user=request.user)
        serializer = SelfUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request):
        user = get_object_or_404(self.queryset, user=request.user)
        serializer = SelfUserSerializer(user)
        serializer.save(role=request.user.role)
