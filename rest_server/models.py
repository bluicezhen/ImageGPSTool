from django.contrib import admin
from django.db import models


class FileModel(models.Model):
    class Meta:
        db_table = 'file'

    title = models.CharField(max_length=512)


admin.site.register(FileModel)
