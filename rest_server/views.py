from rest_framework import mixins, viewsets
from rest_server import models, serializers, settings
from qiniu import Auth as QiniuAuth


class FileViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = models.FileModel.objects.all()
    serializer_class = serializers.FileSerializers

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return serializers.FileUpdateSerializers
        return serializers.FileSerializers

    def get_queryset(self):
        if self.action == "list":
            return models.FileModel.objects.filter(is_upload_qiniu=True).all()
        return models.FileModel.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        # Generate image url
        q = QiniuAuth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
        data = response.data
        for item in data["results"]:
            # Need set image style in qiniu to get thumbnail
            # https://developer.qiniu.com/kodo/kb/4069/take-pictures-style-file-authorization-private-space
            base_url = f"http://ifs-test.zlb37.xyz/{item['id']}-300px"
            image_url = q.private_download_url(base_url, expires=3600)
            item["url"] = image_url
            
        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Generate Qiniu Upload key
        q = QiniuAuth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
        key = response.data["id"]
        response.data['qiniu_upload_token'] = q.upload_token(settings.QINIU_BUCKET, key, 3600)

        return response
