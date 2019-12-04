from rest_framework import serializers
from rest_server import models


class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.FileModel
        fields = ('id', 'title')
