# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import mixins, viewsets, filters, serializers
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .serializers import VideoSerializer
from .serializers import UserSerializer
from ..video.models import Video


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer


class VideoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', )

    @detail_route(methods=['post'], url_path='rent')
    def rent_start(self, request, *args, **kwargs):
        video = self.get_object()
        if not video.aviable:
            raise serializers.ValidationError({'error': "Can't rent not aviable Video."})
        return Response({"success": video.rent_start()})

    @detail_route(methods=['post'], url_path='return')
    def rent_end(self, request, *args, **kwargs):
        video = self.get_object()
        if video.aviable:
            raise serializers.ValidationError({'error': "Can't return not rented Video."})
        return Response({"success": video.rent_end()})
