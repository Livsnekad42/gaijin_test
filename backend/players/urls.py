from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PlayerViewSet, GameViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'players', PlayerViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
