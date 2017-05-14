# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import serializers

from ..video.models import Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class VideoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Video
        fields = ('title', 'aviable', 'url', 'id',)
        extra_kwargs = {'aviable': {'read_only': True}}
