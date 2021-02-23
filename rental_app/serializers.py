from rest_framework import serializers
from . import models


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = ('id', 'name')


class BelongingSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ('id', 'name')


class BorrowedSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = ('id', 'what', 'whom', 'when', 'returned')
