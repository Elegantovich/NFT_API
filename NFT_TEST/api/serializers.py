from rest_framework import serializers

from api.models import (
    Token
)


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('media_url', 'owner')
        model = Token
