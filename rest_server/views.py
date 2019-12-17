from rest_framework import mixins, viewsets
from rest_server import models, serializers, settings
from qiniu import Auth as QiniuAuth


class FileViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = models.FileModel.objects.filter(is_upload_qiniu=True).all()
    serializer_class = serializers.FileSerializers

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return serializers.FileUpdateSerializers
        return serializers.FileSerializers

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Generate Qiniu Upload key
        q = QiniuAuth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
        key = response.data["id"]
        response.data['qiniu_upload_token'] = q.upload_token(settings.QINIU_BUCKET, key, 3600)

        return response
