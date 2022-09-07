import base64
import secrets

from django.core.files.base import ContentFile
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=80)
    score = serializers.IntegerField(required=False, blank=True, null=True)
    avatar = serializers.ImageField(read_only=True)
    avatar_upload = serializers.CharField(required=False, write_only=True, allow_null=True)

    def update(self, instance, validated_data):
        avatar_upload = validated_data.pop("avatar_upload", None)

        if avatar_upload is not None:
            if instance.avatar:
                instance.avatar.delete()

            if avatar_upload:
                file_format, data_url = avatar_upload.split(';base64,')
                _filename, _extension = secrets.token_hex(20), file_format.split('/')[-1]
                avatar_file = ContentFile(base64.b64decode(data_url), name=f"{_filename}.{_extension}")
                instance.avatar = avatar_file

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
