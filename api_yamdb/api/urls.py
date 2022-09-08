from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoriesViewSet, GenresViewSet, TitleViewSet

router_v1 = DefaultRouter()
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register(r'genres', GenresViewSet, basename='genres')
router_v1.register(r'categories', CategoriesViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
