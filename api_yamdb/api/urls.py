from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoriesViewSet, GenresViewSet, TitleViewSet
from users.views import UserViewSet, activate, sign_up

router_v1 = DefaultRouter()
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register(r'genres', GenresViewSet, basename='genres')
router_v1.register(r'categories', CategoriesViewSet, basename='categories')
router_v1.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('v1/auth/signup', sign_up, name='signup'),
    path('v1/auth/token', activate, name='token'),
    path('v1/', include(router_v1.urls)),
]
