import base64
import secrets

from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Player, Game


class GameSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=250)
    players_count = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = (
            "id",
            'name',
            'players_count',
        )

    def get_players_count(self, obj):
        return len(Player.objects.filter(game=self.id))


class PlayerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=80)
    score = serializers.IntegerField(required=False, allow_null=True)
    avatar = serializers.ImageField(read_only=True)
    avatar_upload = serializers.CharField(required=False, write_only=True, allow_null=True)
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    is_banned = serializers.BooleanField()

    class Meta:
        model = Player
        fields = (
            "id",
            'username',
            'score',
            'avatar',
            'game',
            'is_banned',
        )

    def update(self, instance, validated_data):
        avatar_upload = validated_data.pop("avatar_upload", None)
        game = validated_data.pop("game", None)

        if avatar_upload is not None:
            if instance.avatar:
                instance.avatar.delete()

            if avatar_upload:
                file_format, data_url = avatar_upload.split(';base64,')
                _filename, _extension = secrets.token_hex(20), file_format.split('/')[-1]
                avatar_file = ContentFile(base64.b64decode(data_url), name=f"{_filename}.{_extension}")
                instance.avatar = avatar_file
        if game is not None:
            if not instance.game:
                game_serializer = GameSerializer(data=game)
                game_serializer.is_valid(raise_exception=True)
                instance.game = game_serializer.save()

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
