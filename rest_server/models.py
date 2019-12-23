from django.contrib import admin
from django.db import models


class FileModel(models.Model):
    class Meta:
        db_table = 'file'

    # TODO: Add EXIF Information
    # TODO: Add Upload time

    title = models.CharField(max_length=512)
    is_upload_qiniu = models.BooleanField(default=False)


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_upload_qiniu')


admin.site.register(FileModel, FileAdmin)
