from django.contrib import admin
from rest_framework import viewsets
from rest_server import models, serializers


class FileViewSet(viewsets.ModelViewSet):
    queryset = models.FileModel.objects.all()
    serializer_class = serializers.FileSerializers
