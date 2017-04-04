# -*- coding: utf-8 -*-
from rest_framework import serializers

from data.models import Message
from accounts.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    text = serializers.CharField(required=True)
    parent_id = serializers.IntegerField(required=False)

    class Meta:
        model = Message
        fields = ('id', 'author', 'text', 'parent_id',)

    def create(self, validated_data):
        validated_data.update({'author': self.context['request'].user})
        return super().create(validated_data)
