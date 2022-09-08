from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Player, Game
from .serializers import PlayerSerializer, GameSerializer


class PlayerViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Player.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = PlayerSerializer

    def retrieve(self, request, pk):
        try:
            player = self.get_queryset().filter(id=pk).get()

        except Player.DoesNotExist:
            return Response({'errors': {
                "detail": ['Not found or permission denied.']
            }}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(
            player,
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer_data = request.data

        serializer = self.serializer_class(
            data=serializer_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):

        players = self.self.get_queryset().all()

        page = self.paginate_queryset(players)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def update(self, request, pk):

        try:
            player = self.get_queryset().filter(id=pk).get()

        except Player.DoesNotExist:
            return Response({'errors': {
                "detail": ['Not found or permission denied.']
            }}, status=status.HTTP_401_UNAUTHORIZED)

        serializer_data = request.data

        serializer = self.serializer_class(
            player,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            player = self.get_queryset().filter(id=pk).get()

        except Player.DoesNotExist:
            return Response({'errors': {
                "detail": ['Not found or permission denied.']
            }}, status=status.HTTP_401_UNAUTHORIZED)

        player.delete()
        return Response({}, status=status.HTTP_200_OK)


class GameViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = GameSerializer

    def retrieve(self, request, pk):
        try:
            game = self.get_queryset().filter(id=pk).get()

        except Game.DoesNotExist:
            return Response({'errors': {
                "detail": ['Not found or permission denied.']
            }}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(
            game,
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer_data = request.data

        serializer = self.serializer_class(
            data=serializer_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):

        games = self.self.get_queryset().all()

        page = self.paginate_queryset(games)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def update(self, request, pk):

        try:
            game = self.get_queryset().filter(id=pk).get()

        except Game.DoesNotExist:
            return Response({'errors': {
                "detail": ['Not found or permission denied.']
            }}, status=status.HTTP_401_UNAUTHORIZED)

        serializer_data = request.data

        serializer = self.serializer_class(
            game,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            game = self.get_queryset().filter(id=pk).get()

        except Game.DoesNotExist:
            return Response({'errors': {
                "detail": ['Not found or permission denied.']
            }}, status=status.HTTP_401_UNAUTHORIZED)

        game.delete()
        return Response({}, status=status.HTTP_200_OK)
