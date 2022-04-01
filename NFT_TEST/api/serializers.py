from rest_framework import serializers
from api.models import Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('id', 'owner', 'media_url', 'tx_hash', 'unique_hash')
        read_only_fields = ('id',)
