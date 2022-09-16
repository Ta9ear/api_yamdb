from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .permissions import IsAdmin
from .serializers import (SignupSerializer, TokenObtainSerializer,
                          UserManageSerializer)
from .tokens import account_activation_token, get_tokens_for_user
from .utils import create_user


@api_view(['POST', ], )
@permission_classes([])
def sign_up(request):
    """Функция для создания учетной записи. Под конец отправляет письмо."""
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        create_user(serializer)
        return Response(request.data, status=status.HTTP_200_OK)
    return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes([])
def activate(request):
    """Функция для активации учетной записи и предоставления токена."""
    serializer = TokenObtainSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        username = serializer.validated_data['username']
        code = serializer.validated_data['confirmation_code']
        try:
            user = User.objects.get(username=username)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is None:
            return Response(
                'User not found',
                status=status.HTTP_404_NOT_FOUND)
        if not account_activation_token.check_token(user, code):
            return Response('Wrong key', status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        token = get_tokens_for_user(user)
        return Response(token, status=status.HTTP_200_OK)
    return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin, ]
    queryset = User.objects.all()
    serializer_class = UserManageSerializer

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            if 'role' in serializer.validated_data:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                serializer.save(role='user')
                return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = User.objects.get(username=pk)
        serializer = UserManageSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = User.objects.get(username=pk)
        serializer = UserManageSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def partial_update(self, request, pk=None):
        user = User.objects.get(username=pk)
        serializer = UserManageSerializer(user,
                                          data=request.data,
                                          partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = User.objects.get(username=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET', 'PATCH'],
            permission_classes=[IsAuthenticated, ])
    def me(self, request):
        user = User.objects.get(username=request.user)
        if request.method == 'PATCH':
            serializer = UserManageSerializer(user,
                                              data=request.data,
                                              partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        serializer = UserManageSerializer(user)
        return Response(serializer.data)
